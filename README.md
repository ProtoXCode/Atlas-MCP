# Atlas-MCP
> A Model Context Protocol Framework (Sort of?)

Inspired by Walker Reynolds app showcased in a recent YouTube video about the
REAL impact of agentic AI's, and VSCode's Lets Learn MCP in Python.

*I say inspired because I'm not directly following anything to the letter.*

---

## About this project

> This is under heavy development, figuring out stuff as I go along.

I'm not doing this because it's easy, but because I **think** it's easy.
At least that was what I thought before I started.

As I work in a factory where we have no machined hooked up it's basically in
industry 3.0 still. The ERP is new, but no machine integration.

As I'm still new to programming (It's a hobby on the side, I still work
full-time on the factory floor) I see this as a good project to learn more
about this topic. I know first-hand four of the machines I run uses Beckhoff
units. TwinCat 2, 3 and Lightbus on the oldest one. I also got some books on 
MQTT, Industrial IIoT and Industry 4.0 in general. So I've been thinking about
this already. I was also considering Machine Learning class part-time, but
with the current projects I don't have the time. I have a book on that too though.

---

### Project Layout so far (Basic):
 - [x] FastAPI backend
 - [ ] MCP server (Kinda not working so far, client_session problem)
 - [x] Ollama Llama3 offline AI (Offline)
 - [ ] Agents
   - [ ] Discover devices
   - [ ] Connection
   - [ ] Generate dashboards/reports
 - [x] Client GUI app
 - [ ] DASH report page?
 - [ ] Simulation

---

### Progress:
I have a rudimentary FastAPI backend that hooks up with a local run AI. There
is an issue with MCP server where client_session is not forwarded to the MCP
from the backend, so now it just a simple prompt and response.

I've made a very simple GUI app so far, it's basically just boilerplate and
basic layout stuff so far. I haven't worked much with PySide6 before, mostly
Tkinter and CustomTkinter, so there's a learning experience there.

I'm trying to keep the source code in such a way that it will be "easy" to
build on it, so I try to keep it as modular as possible.

---

### Endgame:
Make a program that can discover and set up connections to devices found on
the network and generate dashboards using local run agents.

And of course, learn new stuff along the way.

---

### Resources to inspiration:
 - [The REAL Impact of Agentic AI](https://www.youtube.com/watch?v=5nZyYmiLMyg)
 - [Microsoft Reactor MCP Events](https://developer.microsoft.com/en-us/reactor/?search=mcp&eventLanguage=English&page=1)
 - [Let's Learn MCP Python](https://developer.microsoft.com/en-us/reactor/events/26116/)
 - [Let's learn MCP Python Repo](https://aka.ms/letslearnmcp-python)
