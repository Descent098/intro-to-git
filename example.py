from ezprez.core import *
from ezprez.components import *

# Intro
Slide("Who am I?", "I'm kieran, and I'm a student at the university who uses git and GitHub nearly every day")
Slide("What are we going to do today", ["Learn about version management", "Teach you how to use git and GitHub", "Provide you with some references to come back and learn more"])
Slide("Some setup steps", Raw(r"<p>If you haven't yet please <a href='https://github.com/signup' target=_blank>sign up for a GitHub account</a>, and <a href='https://desktop.github.com/' target=_blank>download Github Desktop</a> if you want to participate in the demo</p>"))

## Version Management
Slide("Version Management", background="facebook")
Slide("What is Version Management?", "Some examples include", ["Android/IOS", "Google Docs", "Almost any App or Software"], background="facebook")
Slide("Why keep old versions?", "It may seem redundant to keep old versions, but there are good reasons like:", ["If only old versions worked for old systems", "If new versions have a major break in them you can rollback", "If people preferred how the old system operated", "etc..."], background="facebook")

### Story
Slide("A story of how not to do it", "When I was but a wee lad...", background="facebook")
Slide("Lessons learned so far", ["I REALLY don't know italian", "Keeping dated backups is handy", "version management helps me see how far I've come"], background="facebook")
Slide("Issues with this Version Management System", ["Copies of project start taking up a lot of space", "Ordered by date, so have to dig through to see what's been changed", "All documentation of changes was manual, and didn't tell me what actually changed in the files line-by-line"], background="facebook")

## Git to the Rescue
Slide("This is where Git comes in", "git is a tool that makes version management MUCH simpler", background="facebook")
Slide("Why is git better?", "compared to my old system git will let you", ["Uses much less space", "go back in time easily", "multiple versions", "let's you add messages so you know what each change was at a glance", "have people download 1 set of files to run your project"], background="facebook")

Slide("Terms", ["<strong>Repo/Repository</strong>: Basically just a fancy name for a folder where the changes are tracked with git"], background="facebook") ###TODO: Add info about terms like repo etc.
Slide("How can I use git?", "There are a few options, you can either use it at the command line (I will call it the CLI version which can be downloaded <a href='https://git-scm.com/downloads', target=_blank>here</a>), or you can use a visual app like <a href='https://desktop.github.com/' target=_blank>GitHub Desktop</a>", background="facebook")
Slide("How does git work? (CLI Version)", "The very basics of git are super simple just", Raw(r'<ol><li style="text-align: left;">Init your repo using: <br><pre><code class="language-bash">git init "project-name"</code></pre></li><br><li style="text-align: left;">Once you have added/changed/deleted your files you add them to "the stage" (also called staging your files) with: <br><pre><code class="language-bash">git add .</code></pre>(The . means add everything in this folder)</li><br> <li style="text-align: left;">Commit your staged changes to the git history with a message using <br><pre><code class="language-bash">git commit -m "Your message goes here"</code></pre></li></ol>'), background="facebook")
# TODO: maybe make the above slide an image

# Setup the presentation
presentation_title = "Introduction to Git & GitHub"
presentation_url = "https://kieranwood.ca/intro-to-git"
presentation_description = f"Slides are available at <a href='{presentation_url}' target=_blank>{presentation_url}</a><br><br>If you want to participate during the demo please also:<br><a href='https://github.com/signup' target=_blank>signup for a GitHub account</a>, and <a href='https://desktop.github.com/' target=_blank>download Github Desktop</a>"
prez = Presentation(presentation_title, presentation_description, presentation_url, background="black")

# Export the files to the current directory at /Presentation, do not change this if you want to use the auto-deployment
prez.export(".", force=True, folder_name="Presentation")



