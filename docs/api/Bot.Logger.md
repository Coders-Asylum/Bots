# <a id="Bot_Logger"></a> Namespace Bot.Logger

### Classes

 [Logger](Bot.Logger.Logger.md)

Logger to log messages to App Insights and to console.
This is added as a singleton service in Program.cs
and can be injected in any class.
<example> 
Usage:
<pre><code class="lang-csharp">public class SomeClass
{
private readonly Logger _logger;
public SomeClass(Logger logger)
{
_logger = logger;
}
public void SomeMethod()
{
_logger.Log.LogInformation("Some message");
}
}</code></pre>
</example>

