# <a id="Bot_Src_Utils_Authentication"></a> Class Authentication

Namespace: [Bot.Src.Utils](Bot.Src.Utils.md)  
Assembly: Bots.dll  

Authentication related utilities.

```csharp
public class Authentication
```

#### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) ← 
[Authentication](Bot.Src.Utils.Authentication.md)

#### Inherited Members

[object.Equals\(object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\)), 
[object.Equals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.equals\#system\-object\-equals\(system\-object\-system\-object\)), 
[object.GetHashCode\(\)](https://learn.microsoft.com/dotnet/api/system.object.gethashcode), 
[object.GetType\(\)](https://learn.microsoft.com/dotnet/api/system.object.gettype), 
[object.MemberwiseClone\(\)](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone), 
[object.ReferenceEquals\(object?, object?\)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals), 
[object.ToString\(\)](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Methods

### <a id="Bot_Src_Utils_Authentication_DecodePrivatePEMKey_System_String_"></a> DecodePrivatePEMKey\(string\)

Decodes the private key from the PEM format.

```csharp
public static RSA DecodePrivatePEMKey(string privateKey)
```

#### Parameters

`privateKey` [string](https://learn.microsoft.com/dotnet/api/system.string)

The PEM file/string contents.

#### Returns

 [RSA](https://learn.microsoft.com/dotnet/api/system.security.cryptography.rsa)

RSA object

### <a id="Bot_Src_Utils_Authentication_GenerateSignedJWTToken_System_String_System_String_"></a> GenerateSignedJWTToken\(string, string\)

Generates the singned JWT token, Using the private key.

```csharp
public static string GenerateSignedJWTToken(string payload, string privateKey)
```

#### Parameters

`payload` [string](https://learn.microsoft.com/dotnet/api/system.string)

`privateKey` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### Returns

 [string](https://learn.microsoft.com/dotnet/api/system.string)

### <a id="Bot_Src_Utils_Authentication_IsTokenExpired_System_String_"></a> IsTokenExpired\(string\)

Checks if the given token is expired or not

```csharp
public static bool IsTokenExpired(string token)
```

#### Parameters

`token` [string](https://learn.microsoft.com/dotnet/api/system.string)

#### Returns

 [bool](https://learn.microsoft.com/dotnet/api/system.boolean)

