Title: Data does not exist unless it exists in three places

## Avoid screaming!

Few things are more miserable than losing work.

The internet is full of sad, sad stories of people who have lost hours,
days, weeks or more of their lives, often through no fault of their own.

Many years ago I heard an MP3 of an answering machine message from some poor sap
who explained, in increasing agitated terms, that the only copy of a book he had
worked on for years was on a disk that a shop had formatted. Fairly quickly he
was reduced to screaming and weeping.

No one wants to be that person.  So listen to my words:

# Data does not exist unless it exists in three places!

I've been giving this advice for decades, except I used to say, "Data does not
exist unless it exists in _two_ places," but I learned better through other people's
experience.

## A few nightmares amongst many

* A power surge during backup destroys your drive and your backup at the same
time.

* Your accounts at [BigDataCompany] are frozen due to a mistake that is not yours.
You have no recourse.  Your email address is no longer accessible, and your
offsite backups are attached to your email address.

* A water leak or file destroys your computer and the backup.

* A thief steals your computer and your backup.

* You erase an important file, and don't notice, and it gets erased from your
online backups, but a year later you desperately need it.


## How to count to three

### Physical backup: onsite

"Onsite" means "physically stored with the computer that is being backed up".

You get a program that runs continuously, copying your main disk to a backup.
MacOS has its Time Machine, Windows has its Backup and Restore, or there are
many others, sorry I can't investigate all the possibilities.

Disks are very cheap, particularly old slow ones.  If you can, get two and rotate:
have two of backup disks, and switch between them every couple of days.

### Physical backup: offsite

Get a backup buddy, a physical person you know who has your backup!
Every once in a while, exchange a current backup of your system with your
backup buddy.

If you don't trust your buddy, you can encrypt the backups.

### Internet backup: cloud

The big data providers give some free space for cloud backup and then will
give you more if you ask.

There are also up-and-coming backup services who charge less, but more
important, actually seem to answer questions. If there's an actual human, you
might have a chance of proving who you are if, for example, you lose your
ememail address (see above).

This is why I switched from the big data to a smaller backup centered service
with good reviews. But who knows if someone who is good today will be good next
year or ten years from now?

### Internet backup: git

Every bit of programming I do gets instantly committed, and then pushed to an
offsite repo, as do my configuration files (dotfiles) for my machine.

If I woke up in Australia with an empty new computer, I could continue from
where I left off in a small number of minutes.


## Remember your work is much more important than your system

It is very useful to have a backup of your whole system software ready to go if
your drive dies.

However, in the worst case you can find another computer, but your work cannot
be replaced.

Prioritize saving your work first.

If you are a writer, a programmer, or even sometimes a musician, It is often the
case that your disk is huge but your current work will fit on a cheap and tiny
thumb drive.

Take advantage of this to copy it to a thumb drive and mail it to someone you
trust, or encrypt it and mail it to someone you trust at least not to reformat
the drive, or (with someone's permission), copy a compressed version of your work
onto their machine when you are there.

Conversely, if your friend is over and you know they are a technological
incompetent, offer to back up their system in your backup system.

I have copied a lot of people's work that way, and I rescued thousands of one
person's photos over decades that would otherwise have been permanently lost.

This alone was worth all the fuss.
