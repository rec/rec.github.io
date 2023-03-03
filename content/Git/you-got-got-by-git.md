Title: You got got by Git!, or, why you need a Git sandbox

Another sad story you see all the time in places like Reddit goes like this: "I
have X amount of work in a git repository, and I did this thing, and there was
this error, and I kept going, and now all my work is gone!"

Git is surprisingly good at not destroying your work, given half a chance, and a
lot of the time people helping the victim can retrieve the data - but sometimes
not.

Git is a powerful program that lets you rearrange huge numbers of files in the
blink of an eye and so it's important to have a basic but solid understanding of
how it works.

 People find version control stressful because you can lose work! It's a very
rational thing to be nervous about, and one part of the solution is a bit of
practice in a safe space before you go under live fire.

## The Git sandbox and the Git notebook

By the time your work is in Git and there is a problem, it is too late for
trial and error with git.

If you use Git, you should have at least one Git sandbox - a git repository with
_fake_ work in it, a repo with nothing to lose, a lot of branches and
meaningless commits - a place for you to experiment with potentially destructive
ideas like `git rebase` and `git reset --hard` and handling merge conflicts and
all sorts of other things that are very stressful to experiment on with your
actual work.

And you should have a Git notebook - somewhere you write down your experiments
as you go. What that "notebook" is exactly depends entirely on you. If you find
Git fascinating and use it all the time, the notebook might be your own brain
but most of us would get more use out of some sort of document, a physical
notebook conceivably, a text file somwhere, some cloud document - somewhere
useful to you.

(Also, make sure to have a recent version of Git. Everything is perfectly
backward compatible but there are some very useful features in later versions,
particularly `git-switch` and `git-restore`, two commands which replace the one
weird `git-checkout` command, which does too many things and is easy to wreak
havoc with.)

## How to play in your new sandbox

Instead of doing a little bit of everything, I strongly suggest digging a bit
deeper into individual commands, a few at a time.

Don't get me wrong here - you probably won't master any Git command in the first
run through like this, but you might want to play with just a few toys at a time
until you get the hang of them.

You should always start with the [man pages](https://git-scm.com/docs) when you
are experimenting with a command.  Do not accept some simplified substitute.

But don't expect to master any of those man pages on the first, or the sixth,
time you see them - don't stress, look for what you need in the page, and don't
feel silly if you have to go over the pages multiple times.

## When Git things go wrong in your work repo

STOP and don't change anything!  Consider duplicating the entire directory to
have a backup in case you make things worse.

Take the series of commands that got you into trouble, and take them to your
sandbox.  Try to make the bad thing happen again, and then experiment with
different ways to get out of it.

Only once you are comfortable again
