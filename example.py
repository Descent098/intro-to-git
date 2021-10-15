from ezprez.core import *
from ezprez.components import *

# Intro
Slide("Who am I?", "I'm kieran, and I'm a student at the university who uses git and GitHub nearly every day")
Slide("What are we going to do today", ["Making sure you are set up with GitHub Desktop", "What is Git/GitHub and why would you want to use it?", "Overview of the Git workflow", "Hands-on demo using GitHub", "Some extra features of Git"])
Slide("Some setup steps", Raw(r"<p>If you haven't yet please <a href='https://github.com/signup' target=_blank>sign up for a GitHub account</a>, and <a href='https://desktop.github.com/' target=_blank>download Github Desktop</a> if you want to participate in the demo</p> <style>ul>li{padding-top: 3px;padding-bottom: 3px;}ol{font-size:x-large;}ul{font-size:x-large;}ol>li{text-align: justify;}</style>"))

## Version Management
Slide("Version Management", background="facebook")
Slide("What is Version Management?", "Version management refers generally to systems that help track changes in a project, and/or different versions", Image("version management", "version_management.png"),background="facebook")
Slide("Why keep old/different versions?", "It may seem redundant to keep old versions, but there are good reasons like:", ["If only old versions worked for old systems", "If new versions have a major break in them you can rollback", "If people preferred how the old system operated", "etc..."], Image("python versions", "python_versions.png"),background="facebook")
Slide("Comes in many shapes and sizes", Raw(r"<br><h4 style='font-style: italic'>Naming systems</h4>"), ["Dates August 2017, Q2 2019, October 14 2021 etc.", "IOS 7, 8, 9, 10 etc.", "Python 2.4, 2.5, 2.6, 2.7, 3.0, 3.1 etc.", "Android KitKat, Lollipop, Marshmallow etc."], Raw("<br><br><h4 style='font-style: italic'>Software To Help do version management:</h4>"), ["Git (Most important!), SVN, Mercurial, Perforce","Google Docs, Google Sheets, OneDrive etc.","Many more..."], background="facebook")


### Story
Slide("A story of how not to do it", "When I was but a wee lad...", Image("Story", "story.png"), background="facebook")
Slide("Lessons learned so far", ["I REALLY don't know italian", "Keeping dated backups is handy", "version management helps me see how far I've come"], background="facebook")
Slide("Issues with this Version Management System", ["Copies of project start taking up a lot of space", "Ordered by date, so have to dig through to see what's been changed", "All documentation of changes was manual, and didn't tell me what actually changed in the files line-by-line", "If someone wanted to help me they would have to download each update folder by folder to have old versions", "Using Google Translate instead of asking someone who spoke Italian what the software said... (not fixed by version management)"], background="facebook")

## Git to the Rescue
Slide("This is where Git comes in", "git is a tool that makes version management MUCH simpler", background="grey")
Slide("Why is git better?", "compared to my old system git will let you", ["Uses much less space", "Go back in time easily", "Multiple versions", "Let's you add messages so you know what each change was at a glance", "Collaborate easily with tools like GitHub", "Ubiquitous system"], background="grey")

### Terms
Slide("Terms", ["<strong>Repo/Repository</strong>: Basically just a fancy name for a folder where the changes are tracked with git", "<strong>Commit</strong>: ", "<strong>Staging Area</strong>: "], background="grey") ###TODO: Add info about terms like repo etc.


## Usage
Slide("Usage", background="red")
Slide("How can I use git?", "There are a few options, you can either use it at the command line (I will call it the CLI version which can be downloaded <a href='https://git-scm.com/downloads', target=_blank>here</a>), or you can use a visual app like <a href='https://desktop.github.com/' target=_blank>GitHub Desktop</a>", background="red")

### Git flow
Slide("Git Flow", Raw("<ol class='content-center'><li> Create or <strong>clone</strong> a repo</li> <li><strong>Add</strong> our changes that we want to save</li> <li><strong>Commit </strong>(save) our changes</li> <li><strong>Push</strong> our commit</li> <li>Repeat steps 2 - 4 as you develop your project</li></ol>"), background="white")
Slide("Git Flow", Image("flow", "flow.png"), background="white")

#### More detailed view

# TODO: Add pictures of folder at each step
Slide("Step 1; Git Init/Clone", "We use this command to create a new repository <br><br>You can think of a repository as a folder that holds all the files you are interested in managing", background="white")
Slide("Step 2; Add Your Changes", "Change your files, this can be any <strong>CUD</strong> operations (Create, update, delete), then <strong>add them to the staging area</strong>",Image("add", "add.png"), background="white")
Slide("Step 3; Commit Changes", "Saving the changes we stored in the staging area is called <strong>committing</strong> your changes",Image("commit", "commit.png"), background="white")
Slide("Step 4; Push Changes", "Once your changes are committed, you can push them to the remote repository. Once they are pushed, your teammates can start working off of the changes you made!",Image("push", "push.png"), background="white")




## Demo
Slide("Demo", background="purple")
# TODO: ADD IMAGES
Slide("What we're going to do", Raw("<ol class='content-center'><li>Create a repo on github</li> <li>Clone it locally</li> <li>Make some changes</li> <li>Add & Commit the changes</li> <li>Push the changes to github</li></ol>"), background="purple")
Slide("Step 1; Git Init on GitHub","Head to github.com and login. Then hit the + in the corner and click on New Repository", background="purple")
Slide("Step 1; Git Init on GitHub",["Enter a name", "Enter a description", "Choose public or private", "And check off the box for", "Add a README file", "Hit Create Repository"], background="purple")
Slide("Step 1.5; Git Clone", "Now we need to get the files locally, to do this go into GitHub Desktop and hit File --> Clone Repository. This should load a list of your projects on Github and let you select where to put the files (hit refresh if it's not there).", background="purple")
Slide("Step 2; Make & Add Changes","Go wherever you saved the repository and edit the README.md file to add what you want (any text editor like Notepad or TextEdit will work). GitHub desktop combines adding your changes with the next step by selecting the changed files in the program.", background="purple")
Slide("Step 3; Commit your changes","Now you have added your files you need to add a commit message (and optionally a description), and then hit Commit to main", background="purple")
Slide("Step 4; Push your changes", "Now the changes are made you can push them to your repo, and you will see the changes on GitHub (remember to tell others to pull when you make a change)!", background="purple")



## Extra Features
Slide("Extra Features", background="green")

### Branches
Slide("Branches", background="green")
### Merging
Slide("Merging", background="green")

### At the CLI
Slide("Using Git Remotely at the command line", background="green")
Slide("How does the git command line work?", "The flow is the same, you just run the following commands", Raw(r'<ol><li style="text-align: left;">Create the repo in GitHub Desktop or on the GitHub site</li><br><li style="text-align: left;">Clone the repository using GitHub desktop, or <br><pre><code class="language-bash">git clone https://github.com/username/repo-name</code></pre></li><br><li style="text-align: left;">Once you have added/changed/deleted your files you add them to "the stage" (also called staging your files) with: <br><pre><code class="language-bash">git add .</code></pre>(The . means add everything in this folder)</li><br> <li style="text-align: left;">Commit your staged changes to the git history with a message using <br><pre><code class="language-bash">git commit -m "Your message goes here"</code></pre></li> <br><li style="text-align: left;">Push your commits in Github Desktop, or at the command line using <br><pre><code class="language-bash">git push</code></pre></li></ol>'), background="green")

## More things to look into
Slide("More things to look into", background="blue")

### Open source
Slide("Open Source", background="blue")

### CI/CD
Slide("CI/CD", background="blue")

# Setup the presentation
presentation_title = "Introduction to Git & GitHub"
presentation_url = "https://kieranwood.ca/intro-to-git"
presentation_description = f"Slides are available at <a href='{presentation_url}' target=_blank>{presentation_url}</a><br><br>If you want to participate during the demo please also:<br><a href='https://github.com/signup' target=_blank>signup for a GitHub account</a>, and <a href='https://desktop.github.com/' target=_blank>download Github Desktop</a>"
prez = Presentation(presentation_title, presentation_description, presentation_url, background="black")

# Export the files to the current directory at /Presentation, do not change this if you want to use the auto-deployment
prez.export(".", force=True, folder_name="Presentation")

if __name__ == "__main__":
    from webbrowser import open as web_open
    import os
    web_open(os.path.abspath(os.path.join("Presentation", "index.html")))

