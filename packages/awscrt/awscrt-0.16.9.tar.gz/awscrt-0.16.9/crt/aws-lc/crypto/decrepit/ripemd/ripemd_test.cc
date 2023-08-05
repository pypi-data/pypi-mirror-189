/* Copyright (c) 2016, Google Inc.
 *
 * Permission to use, copy, modify, and/or distribute this software for any
 * purpose with or without fee is hereby granted, provided that the above
 * copyright notice and this permission notice appear in all copies.
 *
 * THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
 * WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY
 * SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
 * WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
 * OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
 * CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. */

#include <openssl/ripemd.h>

#include <memory>

#include <stdio.h>
#include <string.h>

#include <gtest/gtest.h>

#include "../../internal.h"
#include "../../test/test_util.h"


struct RIPEMDTestCase {
  const char *input;
  uint8_t expected[RIPEMD160_DIGEST_LENGTH];
};

static const RIPEMDTestCase kRIPEMDTestCases[] = {
    {"", {0x9c, 0x11, 0x85, 0xa5, 0xc5, 0xe9, 0xfc, 0x54, 0x61, 0x28,
          0x08, 0x97, 0x7e, 0xe8, 0xf5, 0x48, 0xb2, 0x25, 0x8d, 0x31}},
    {"a", {0x0b, 0xdc, 0x9d, 0x2d, 0x25, 0x6b, 0x3e, 0xe9, 0xda, 0xae,
           0x34, 0x7b, 0xe6, 0xf4, 0xdc, 0x83, 0x5a, 0x46, 0x7f, 0xfe}},
    {"abc", {0x8e, 0xb2, 0x08, 0xf7, 0xe0, 0x5d, 0x98, 0x7a, 0x9b, 0x04,
             0x4a, 0x8e, 0x98, 0xc6, 0xb0, 0x87, 0xf1, 0x5a, 0x0b, 0xfc}},
    {"message digest",
     {0x5d, 0x06, 0x89, 0xef, 0x49, 0xd2, 0xfa, 0xe5, 0x72, 0xb8,
      0x81, 0xb1, 0x23, 0xa8, 0x5f, 0xfa, 0x21, 0x59, 0x5f, 0x36}},
    {"abcdefghijklmnopqrstuvwxyz",
     {0xf7, 0x1c, 0x27, 0x10, 0x9c, 0x69, 0x2c, 0x1b, 0x56, 0xbb,
      0xdc, 0xeb, 0x5b, 0x9d, 0x28, 0x65, 0xb3, 0x70, 0x8d, 0xbc}},
    {"abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq",
     {0x12, 0xa0, 0x53, 0x38, 0x4a, 0x9c, 0x0c, 0x88, 0xe4, 0x05,
      0xa0, 0x6c, 0x27, 0xdc, 0xf4, 0x9a, 0xda, 0x62, 0xeb, 0x2b}},
    {"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789",
     {0xb0, 0xe2, 0x0b, 0x6e, 0x31, 0x16, 0x64, 0x02, 0x86, 0xed,
      0x3a, 0x87, 0xa5, 0x71, 0x30, 0x79, 0xb2, 0x1f, 0x51, 0x89}},
    {"1234567890123456789012345678901234567890123456789012345678901234567890123"
     "4567890",
     {0x9b, 0x75, 0x2e, 0x45, 0x57, 0x3d, 0x4b, 0x39, 0xf4, 0xdb,
      0xd3, 0x32, 0x3c, 0xab, 0x82, 0xbf, 0x63, 0x32, 0x6b, 0xfb}},
};

// TODO(davidben): Convert this file to GTest properly.
TEST(RIPEMDTest, RunTest) {
  unsigned test_num = 0;
  int ok = 1;

  for (const auto &test : kRIPEMDTestCases) {
    test_num++;

    const size_t input_len = strlen(test.input);

    for (size_t stride = 0; stride <= input_len; stride++) {
      uint8_t digest[RIPEMD160_DIGEST_LENGTH];

      if (stride == 0) {
        RIPEMD160(reinterpret_cast<const uint8_t *>(test.input), input_len,
                  digest);
      } else {
        RIPEMD160_CTX ctx;
        RIPEMD160_Init(&ctx);

        for (size_t done = 0; done < input_len;) {
          const size_t remaining = input_len - done;
          size_t todo = stride;
          if (todo > remaining) {
            todo = remaining;
          }

          RIPEMD160_Update(&ctx, &test.input[done], todo);
          done += todo;
        }

        RIPEMD160_Final(digest, &ctx);
      }

      if (OPENSSL_memcmp(digest, test.expected, sizeof(digest)) != 0) {
        fprintf(stderr, "#%u: bad result with stride %u: ", test_num,
                static_cast<unsigned>(stride));
        hexdump(stderr, "", digest, sizeof(digest));
        ok = 0;
      }
    }
  }

  static const size_t kLargeBufSize = 1000000;
  std::unique_ptr<uint8_t[]> buf(new uint8_t[kLargeBufSize]);
  OPENSSL_memset(buf.get(), 'a', kLargeBufSize);
  uint8_t digest[RIPEMD160_DIGEST_LENGTH];
  RIPEMD160(buf.get(), kLargeBufSize, digest);

  static const uint8_t kMillionADigest[RIPEMD160_DIGEST_LENGTH] = {
      0x52, 0x78, 0x32, 0x43, 0xc1, 0x69, 0x7b, 0xdb, 0xe1, 0x6d,
      0x37, 0xf9, 0x7f, 0x68, 0xf0, 0x83, 0x25, 0xdc, 0x15, 0x28};

  if (OPENSSL_memcmp(digest, kMillionADigest, sizeof(digest)) != 0) {
    fprintf(stderr, u8"Digest incorrect for “million a's” test: ");
    hexdump(stderr, "", digest, sizeof(digest));
    ok = 0;
  }

  EXPECT_EQ(1, ok);
}
