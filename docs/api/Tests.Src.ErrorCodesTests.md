# <a id="Tests_Src_ErrorCodesTests"></a> Class ErrorCodesTests

Namespace: [Tests.Src](Tests.Src.md)  
Assembly: Bots.dll  

Tests for ErrorCodes class. simple tests to check that the error codes are returned in the correct format.

```csharp
public class ErrorCodesTests
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[ErrorCodesTests](Tests.Src.ErrorCodesTests.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Methods

### <a id="Tests_Src_ErrorCodesTests_ErrorCodes_ReturnsString_InUpperCase"></a> ErrorCodes\_ReturnsString\_InUpperCase\(\)

Tests that the error codes are string and in upper case.

```csharp
[Fact]
public void ErrorCodes_ReturnsString_InUpperCase()
```

### <a id="Tests_Src_ErrorCodesTests_ErrorCodes_ReturnsString_WithoutSpaces"></a> ErrorCodes\_ReturnsString\_WithoutSpaces\(\)

Tests that the error codes does not contain spaces.

```csharp
[Fact]
public void ErrorCodes_ReturnsString_WithoutSpaces()
```

