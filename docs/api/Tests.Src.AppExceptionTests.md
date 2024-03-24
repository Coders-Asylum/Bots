# <a id="Tests_Src_AppExceptionTests"></a> Class AppExceptionTests

Namespace: [Tests.Src](Tests.Src.md)  
Assembly: Bots.dll  

```csharp
public class AppExceptionTests
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[AppExceptionTests](Tests.Src.AppExceptionTests.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Constructors

### <a id="Tests_Src_AppExceptionTests__ctor"></a> AppExceptionTests\(\)

```csharp
public AppExceptionTests()
```

## Methods

### <a id="Tests_Src_AppExceptionTests_AppException_InternalError_ReturnsException"></a> AppException\_InternalError\_ReturnsException\(\)

```csharp
[Fact]
public void AppException_InternalError_ReturnsException()
```

### <a id="Tests_Src_AppExceptionTests_AppException_LogsError"></a> AppException\_LogsError\(\)

Tests that the error is logged to the logger and verfies that the logged string contains the error code, message and the inner error message.

```csharp
[Fact]
public void AppException_LogsError()
```

### <a id="Tests_Src_AppExceptionTests_AppException_ModifiesMessage_WithException"></a> AppException\_ModifiesMessage\_WithException\(\)

```csharp
[Fact]
public void AppException_ModifiesMessage_WithException()
```

### <a id="Tests_Src_AppExceptionTests_AppException_ModifiesMessage_WithoutException"></a> AppException\_ModifiesMessage\_WithoutException\(\)

```csharp
[Fact]
public void AppException_ModifiesMessage_WithoutException()
```

### <a id="Tests_Src_AppExceptionTests_GetErrorResponse_ReturnsCorrectErrorResponse"></a> GetErrorResponse\_ReturnsCorrectErrorResponse\(\)

```csharp
[Fact]
public void GetErrorResponse_ReturnsCorrectErrorResponse()
```

