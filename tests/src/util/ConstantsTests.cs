// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using Xunit;
using Bots.Src.Utils;

namespace Tests.Src.Utils
{
    public class ConstantsTests
    {

        [Fact]
        public void TestConstants()
        {
            Assert.Equal("CONFIG_PATH", Constants.CONFIG_PATH_ENV);
        }

        [Fact]
        public void TestAlgorithmsConstants()
        {
            Assert.Equal("RS256", Algorithms.RS256);
            Assert.Equal("RS384", Algorithms.RS384);
        }

        [Fact]
        public void TestHTTPStatusConstants()
        {
            Assert.Equal(200, HTTPStatus.OK);
            Assert.Equal(201, HTTPStatus.CREATED);
            Assert.Equal(400, HTTPStatus.BAD_REQUEST);
            Assert.Equal(401, HTTPStatus.UNAUTHORIZED);
            Assert.Equal(403, HTTPStatus.FORBIDDEN);
            Assert.Equal(404, HTTPStatus.NOT_FOUND);
            Assert.Equal(500, HTTPStatus.INTERNAL_SERVER_ERROR);
            Assert.Equal(503, HTTPStatus.SERVICE_UNAVAILABLE);
            Assert.Equal(504, HTTPStatus.GATEWAY_TIMEOUT);
        }
    }
}