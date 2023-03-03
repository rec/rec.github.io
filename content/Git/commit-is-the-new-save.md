Title: Commit is the new save

## [Data does not exist unless it exists in three
places.](data-does-not-exist-unless-it-exists-in-three-places.html)

And if you wipe out even half an hour's work on one file, the result is more
than a half an hour lost, due to loss of flow and momentum and energy.

There is also the end-of-session slip, which is well-known in more athletic
fields like rock climbing - errors are more common at the end of a programming
session because you are tired and pushing to clean up.

And the complementary start-of-session confusion, when you don't remember
where you left off.

Or you get everything working, and then you decide you need to make a clean-up
change, and then it stops working, and you can't get it working again, and you
haven't committed in two hours, and you just want to go home...

Or you might get called up on a great adventure in exotic lands, and have to
leave your computer behind with no warning.  It happens all the time.

## Commit is the new save.

* Work on a separate branch
* Push new commits to a remote almost continuously
* Squash and rebase down into a few carefully named commits at the end

Having your tiny steps saved fixes the "half an hour lost" and "got it working
then broke it" and "dragonslayer" scenarios.

"In the morning", when you start a new programming session, you look back at the
last few commits you wrote before you left off, which should be small and only
touch one or two files. You can both see what you did at the end, and if it was
bad, quickly rebase it out of existence before anyone notices.

As a bonus, in the "then broke it" scenario, you can possibly use `git bisect`
to track down the error automatically.

## How does it work?

Top-level view - for every feature, sketch, or idea:

* Create a brand-new branch and push it to a remote
* Any time you do any work, commit and push
    * It's nice if none of these commit points breaks your unit tests, but not
necessary
* Continue working until coding is done
* Rebase commits into final form
* Start a code review

During review, the same idea holds:
* Start from the commits the reviewers saw
* Then work as usual with tiny commits
* Rebase those commits into
[fixup](https://fle.github.io/git-tip-keep-your-branch-clean-with-fixup-and-autosquash.html)
commits
* Iterate until the reviewers are satisfied
* Then rebase will automatically fold in the fixup commits

## Details

You need each action in this workflow to be as simple as possible so
you stop for a sip of coffee and just naturally save, commit and push.

I have a set of git extensions called [`gitz`](https://github.com/rec/gitz)
written in Python that I use for these purposes, and you can too, but you can do
much the same with aliases or bash scripts.

I start with a new branch which I can push to using
[`git-new`](https://github.com/rec/gitz/blob/main/doc/git-new.rst).

    $ git new tweak-search

If you don't have `git-new`, you'll do something like this, (assuming you are
working with other people on a remote called `upstream` against a branch called
`main`, and your own remote is called `origin`)

    $ git fetch upstream
    $ git checkout -B tweak-search
    $ git push --set-upstream origin tweak-search

Now I make some changes and use either
[`git-infer`](https://github.com/rec/gitz/blob/main/doc/git-infer.rst) to
create a single commit with a vaguely descriptive name, or
[`git-split`](https://github.com/rec/gitz/blob/main/doc/git-split.rst) to
create one commit per file that has changed.

At the end, I make a lot of use of `git rebase -i`, and also my own
[`git-permute`](https://github.com/rec/gitz/blob/main/doc/git-permute.rst),
another gitz extension, probably not for the faint of heart, that lets you permute
and delete commits, so for example, `git permute dca` takes the last four
commits, removes the second most recent commit and reverses the order of the
other three.
