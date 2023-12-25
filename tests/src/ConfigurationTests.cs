// write tests using xunit

using System.Text.Json;
using Bot.Src.Config;
using Xunit;

namespace tests.src
{
    public class ConfigurationTests
    {

        const string configPathEnv1 = "CONFIG_PATH";
        const string configPathEnv2 = "CONFIG_PATH_2";
        const string configPath1 = "../res/config.json";
        const string configPath2 = "../res/config2.json";
        
        /// <summary>
        /// Tests that the config is loaded from the local config file.
        /// </summary>
        /// <exception cref="Exception"></exception>
        [Fact]
        public void TestLoadConfig()
        {
            // Arrange
            // class under test
            Configuration config = new();
            // set config path env variable
            Environment.SetEnvironmentVariable(configPathEnv1, configPath1);
            string configPath = Environment.GetEnvironmentVariable(configPathEnv1) ?? throw new Exception("CONFIG_PATH env variable not found");
            string configFileContents = File.ReadAllText(configPath);
            Dictionary<string, dynamic> expectedConfig = JsonSerializer.Deserialize<Dictionary<string, dynamic>>(configFileContents) ?? throw new Exception("Config file found is empty");

            // Act
            config.LoadConfig();

            // Assert
            Assert.Equal(expectedConfig, config.localConfig);
        }
    }
}