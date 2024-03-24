# <a id="Tests_Src_ConfigurationTests"></a> Class ConfigurationTests

Namespace: [Tests.Src](Tests.Src.md)  
Assembly: Bots.dll  

```csharp
public class ConfigurationTests
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ConfigurationTests](Tests.Src.ConfigurationTests.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Methods

### <a id="Tests_Src_ConfigurationTests_TestHasBeenLoadedFlagIsSetToTrue"></a> TestHasBeenLoadedFlagIsSetToTrue\(\)

Test has been loaded flag is set to true after static constructor is called.

```csharp
[Fact]
public void TestHasBeenLoadedFlagIsSetToTrue()
```

### <a id="Tests_Src_ConfigurationTests_TestLoacalConfigIsLoaded"></a> TestLoacalConfigIsLoaded\(\)

Tests that the config is loaded from the local config file.

```csharp
[Fact]
public void TestLoacalConfigIsLoaded()
```

#### Exceptions

 [Exception](https://learn.microsoft.com/dotnet/api/system.exception)

### <a id="Tests_Src_ConfigurationTests_TestLoadConfigThrowsExceptionIfConfigFileContentsIsNull"></a> TestLoadConfigThrowsExceptionIfConfigFileContentsIsNull\(\)

Exception is thrown if config file contents is null.

```csharp
[Fact]
public void TestLoadConfigThrowsExceptionIfConfigFileContentsIsNull()
```

### <a id="Tests_Src_ConfigurationTests_TestLoadConfigThrowsExceptionIfConfigFileIsNotValidJson"></a> TestLoadConfigThrowsExceptionIfConfigFileIsNotValidJson\(\)

Exception is thrown if config file is not valid json.

```csharp
[Fact]
public void TestLoadConfigThrowsExceptionIfConfigFileIsNotValidJson()
```

### <a id="Tests_Src_ConfigurationTests_TestLoadConfigThrowsExceptionIfConfigPathEnvVariableNotFound"></a> TestLoadConfigThrowsExceptionIfConfigPathEnvVariableNotFound\(\)

Exception is thrown if config path env variable is not found.

```csharp
[Fact]
public void TestLoadConfigThrowsExceptionIfConfigPathEnvVariableNotFound()
```

### <a id="Tests_Src_ConfigurationTests_TestLocalConfigIsLoadedOnce"></a> TestLocalConfigIsLoadedOnce\(\)

Test that once config is loaded, it is not loaded again.

```csharp
[Fact]
public void TestLocalConfigIsLoadedOnce()
```

