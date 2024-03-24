# <a id="Tests_Src_LoggerTests"></a> Class LoggerTests

Namespace: [Tests.Src](Tests.Src.md)  
Assembly: Bots.dll  

Tests for <xref href="Bot.Logger.Logger" data-throw-if-not-resolved="false"></xref>
This not an comprehensive test,just enough to make sure the logger is being created and returned correctly.
Will not be adding more tests unless there is a change in the logger class, related to its format and on a custom functioanlity added to it.

```csharp
public class LoggerTests
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[LoggerTests](Tests.Src.LoggerTests.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Constructors

### <a id="Tests_Src_LoggerTests__ctor"></a> LoggerTests\(\)

```csharp
public LoggerTests()
```

## Methods

### <a id="Tests_Src_LoggerTests_Logger_CreatesLogger_OnConstruction"></a> Logger\_CreatesLogger\_OnConstruction\(\)

```csharp
[Fact]
public void Logger_CreatesLogger_OnConstruction()
```

### <a id="Tests_Src_LoggerTests_Logger_ReturnsLogger_OnGetLog"></a> Logger\_ReturnsLogger\_OnGetLog\(\)

```csharp
[Fact]
public void Logger_ReturnsLogger_OnGetLog()
```

