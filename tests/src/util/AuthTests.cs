// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using Xunit;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using Bot.Src.Utils;


namespace Tests.Src.Utils
{


    public class AuthTests
    {
        [Fact]
        public void TestIsTokenExpired()
        {
            // Arrange
            SymmetricSecurityKey securityKey = new(Encoding.UTF8.GetBytes("ThisIsASecretKeyForEncryption32_"));
            SigningCredentials credentials = new(securityKey, SecurityAlgorithms.HmacSha256);

            var tokenHandler = new JwtSecurityTokenHandler();
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Expires = DateTime.UtcNow.AddMinutes(-1), // Expired token
                SigningCredentials = credentials,
                NotBefore = DateTime.UtcNow.AddMinutes(-5), // Not valid before 5 minutes ago

            };

            string token = tokenHandler.WriteToken(tokenHandler.CreateToken(tokenDescriptor));

            // Act
            bool isExpired = Authentication.IsTokenExpired(token);

            // Assert
            Assert.True(isExpired);
        }
    }

}
