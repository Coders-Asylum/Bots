// write tests using xunit

using System.Text.Json;
using Bot.Src;
using Xunit;


namespace tests.src
{
    public class ConfigurationTests
    {

        const string configPathEnv1 = "CONFIG_PATH";
        const string configPathEnv2 = "CONFIG_PATH_2";
        const string configPath1 = "tests/res/config.json";
        const string configPath2 = "tests/res/config2.json";
        
        /// <summary>
        /// Tests that the config is loaded from the local config file.
        /// </summary>
        /// <exception cref="Exception"></exception>
        [Fact]
        public void TestLoadConfig()
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
        public void TestLocalConfigIsLoadedOnce(){
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
            // Assert HasBeenLoaded is true
            Assert.True(Configuration.HasBeenLoaded);
            // not equivalent to expectedConfig2
            Assert.NotEqual(expectedConfig2, actualConfig);
            // test if second time loaded config is equivalent to first time loaded.
            Assert.Equivalent(expectedConfig1, actualConfig2);
        }

        
    }
}