# Automating GUI Actions

Some notes on automation that might help implement more complication preservation actions, e.g. doing things in desktop applications.

- WinAppDriver
	- [example](https://techcommunity.microsoft.com/t5/testingspot-blog/winappdriver-and-desktop-ui-test-automation/ba-p/1124543)
	- Seems to have been Microsoft supported until a few years ago.
	- I assume this is because Power Automate is now the preferred solution, but this is not open or free (AFAICT).
- Robot Framework:
	- The [windows](https://rpaframework.org/libraries/windows/) module.
	- The [desktop](https://robocorp.com/docs/libraries/rpa-framework/rpa-desktop) module.
	- This doesn't have a GUI, but it is possible to write simple automations in a fairly simple way. Would be good to follow up on LibreOffice example. e.g. can we make one that goes:
		- Load File In LibreOffice.
		- Ensure Tools > Protect Document > Protect Fields is enabled.
		- Print to PDF with a given output filename.

