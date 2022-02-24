# Researching Reasons that NFL Coaches Get Fired

### Parker Dunn (pgdunn@bu.edu & parker_dunn@outlook.com)

## Motivation

Every NFL offseason there is discussion about which coaches deserve to keep there job and why or why not they might be fired. I have heard a lot of logicial reasoning for coaches being fired: (1) lack of improvement, (2) inability to develop a rookie QB, (3) underperforming (obviously). I cannot recall a lot of data supporting the reasons that coaches are typically fired based on historical timings that coaches are fired.

Thus, the original motivation for starting this mini-project was to figure out what set of factors is most consistently responsible for NFL coaches getting fired. My plan is too look at things like:
* Are coaches typically fired within X years of drafting a rooking QB?
* __Do coaches actually extend their lifetime with a team by waiting to draft a rookie QB?__
* Are coaches fired even when they help improve a team? (i.e., are they fired just because they have a bad record and relatively poor performance by their players?)

To investigate these questions, I started looking for information about coaches for each NFL team. I didn't find a convenient way to pull the data from a database (although I may have missed the data in nflfastR somewhere), so I decided to figure out how to scrape data from www.pro-football-reference.com.

My next steps will be...
(1) Cleaning up the coaching data a little
(2) Importing additional data about teams that I pulled from nflfastR
(3) Extracting team stats information -> record, record ATS, EPA info, QB stats, PFF grades (depending on convenience of the data I need)

(4) ... more than this I'm sure depending on what I need