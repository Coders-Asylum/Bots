// Copyright (c) 2023 the CODERS Asylum project authors. All rights reserved.
// Use of this source code is governed by a BSD-style license
// that can be found in the LICENSE file.

using System.Text.Json;
using Bot.Src;
using Xunit;
using Moq;

namespace tests.src
{
    public class ConfigurationTests
    {

        const string configPathEnv1 = "CONFIG_PATH";
        const string configPathEnv2 = "CONFIG_PATH_2";
        const string configPath1 = "tests/res/config.json";
        const string configPath2 = "tests/res/config2.json";
        const string emptyJsonFilePath = "tests/res/empty.json";
        const string invalidJsonFilePath = "tests/res/error.json";


        /// <summary>
        /// Test has been loaded flag is set to true after static constructor is called.
        /// </summary>
        [Fact]
        public void TestHasBeenLoadedFlagIsSetToTrue()
        {
            // Arrange
            // Act
            // Assert
            Assert.True(Configuration.HasBeenLoaded);
        }
        /// <summary>
        /// Tests that the config is loaded from the local config file.
        /// </summary>
        /// <exception cref="Exception"></exception>
        [Fact]
        public void TestLoacalConfigIsLoaded()
        {
            // Arrange
            // set config path env variable
            Environment.SetEnvironmentVariable(configPathEnv1, configPath1);
            string configPath = Environment.GetEnvironmentVariable(configPathEnv1) ?? throw new Exception("CONFIG_PATH env variable not found");
            string configFileContents = File.ReadAllText(configPath);
            Dictionary<string, dynamic> expectedConfig = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(configFileContents) ?? throw new Exception("Config file found is empty");

            // Act
            Dictionary<string, dynamic> actualConfig = Configuration.LocalConfig;

            // Assert
            Assert.Equivalent(expectedConfig, actualConfig);

        }

        /// <summary>
        /// Test that once config is loaded, it is not loaded again.
        /// </summary>
        [Fact]
        public void TestLocalConfigIsLoadedOnce()
        {
            // Arrange
            // set config path env variable
            Environment.SetEnvironmentVariable(configPathEnv1, configPath1);
            string configFileContents1 = File.ReadAllText(configPath1);
            string configFileContents2 = File.ReadAllText(configPath2);

            Dictionary<string, dynamic> expectedConfig1 = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(configFileContents1) ?? throw new Exception("Config file found is empty");
            Dictionary<string, dynamic> expectedConfig2 = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(configFileContents2) ?? throw new Exception("Config file found is empty");
            // Act
            Dictionary<string, dynamic> actualConfig = Configuration.LocalConfig;
            // set config path env varible again for different config file
            Environment.SetEnvironmentVariable(configPathEnv1, configPath2);
            // load config again.
            Dictionary<string, dynamic> actualConfig2 = Configuration.LocalConfig;

            // TESTS
            // Assert equivalent to expectedConfig1
            Assert.Equivalent(expectedConfig1, actualConfig);
            // not equivalent to expectedConfig2
            Assert.NotEqual(expectedConfig2, actualConfig);
            // test if second time loaded config is equivalent to first time loaded.
            Assert.Equivalent(expectedConfig1, actualConfig2);
        }

        /// <summary>
        /// Exception is thrown if config path env variable is not found.
        /// </summary>
        [Fact]
        public void TestLoadConfigThrowsExceptionIfConfigPathEnvVariableNotFound()
        {
            // Arrange
            // unset config path env variable
            Environment.SetEnvironmentVariable(configPathEnv1, null);

            // Act
            // Assert
            Assert.Throws<Exception>(() => Configuration.LoadConfig());
        }

        /// <summary>
        /// Exception is thrown if config file contents is null.
        /// </summary>
        [Fact]
        public void TestLoadConfigThrowsExceptionIfConfigFileContentsIsNull()
        {
            // Arrange
            // set config path env variable
            Environment.SetEnvironmentVariable(configPathEnv1, emptyJsonFilePath);
            // Act
            // Assert
            Assert.Throws<Exception>(() => Configuration.LoadConfig());
        }

        /// <summary>
        /// Exception is thrown if config file is not valid json.
        /// </summary>
        [Fact]
        public void TestLoadConfigThrowsExceptionIfConfigFileIsNotValidJson()
        {
            // Arrange
            // set config path env variable
            Environment.SetEnvironmentVariable(configPathEnv1, invalidJsonFilePath);
            // Act
            // Assert
            Assert.Throws<Exception>(() => Configuration.LoadConfig());
        }


    }
}