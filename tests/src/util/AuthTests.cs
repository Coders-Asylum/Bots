// Copyright (c) 2024 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using Xunit;
using System.IdentityModel.Tokens.Jwt;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using Bot.Src.Utils;
using System.Security.Cryptography;


namespace Tests.Src.Utils
{


    public class AuthTests
    {
        // Arrange
        private readonly string appId = "test_app_id";
        private readonly SymmetricSecurityKey securityKey = new(Encoding.UTF8.GetBytes("ThisIsASecretKeyForEncryption32_"));
        private readonly SigningCredentials hmac256SignedCredentials;

        private readonly string pemKey;

        public AuthTests()
        {
            hmac256SignedCredentials = new SigningCredentials(securityKey, SecurityAlgorithms.HmacSha256);
            using RSA rsa = RSA.Create();
            pemKey = rsa.ExportRSAPrivateKeyPem();
        }
        [Fact]
        public void TestIsTokenExpired()
        {


            var tokenHandler = new JwtSecurityTokenHandler();
            var tokenDescriptor = new SecurityTokenDescriptor
            {
                Expires = DateTime.UtcNow.AddMinutes(-1), // Expired token
                SigningCredentials = hmac256SignedCredentials,
                NotBefore = DateTime.UtcNow.AddMinutes(-5), // Not valid before 5 minutes ago

            };

            string token = tokenHandler.WriteToken(tokenHandler.CreateToken(tokenDescriptor));

            // Act
            bool isExpired = Authentication.IsTokenExpired(token);

            // Assert
            Assert.True(isExpired);
        }

        [Fact]
        public void TestGithubAppJWTToken()
        {
            // Act
            string token = Authentication.GithubAppJWTToken(appId, pemKey);
            JwtSecurityToken jwtToken = new JwtSecurityTokenHandler().ReadJwtToken(token);

            // Assert
            Assert.Equal(appId, jwtToken.Claims.First(claim => claim.Type == "iss").Value);
            Assert.True(long.Parse(jwtToken.Claims.First(claim => claim.Type == "iat").Value) <= DateTimeOffset.UtcNow.ToUnixTimeSeconds());
            Assert.True(long.Parse(jwtToken.Claims.First(claim => claim.Type == "exp").Value) >= DateTimeOffset.UtcNow.ToUnixTimeSeconds());
        }
    }

}
