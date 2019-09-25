# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

-   Have the ability to send to a slack channel instead of printing to the terminal

### [1.0.2] - 2019-09-09

### Added

-   Created new file `functions.py` to take all functions into a seperate file to clean up `app.py`

### Changed

-   Removed all ultity functions from `app.py` for easier reading.

## [1.0.1] - 2019-08-29

### Added

-   Added each logic from the `for` loops. Into functions to clean up the code.
-   Split the cards into their own lists, for easier reading.
-   Used the variables `color`, `status` and `list_ID` as arguements for each function, to make them clearer

### Changed

-   Change `cards = data['cards']` to `cards = data.get('cards')`
-   Readme

### Removed

-   Removed `len(open_tickets['labels']) > 0:` and just used `open_tickets['labels']` as an empty list is falsy.

### Fixed

-   Fixed typo on the `progesss_customer` variable which has too many one too many `s`'s it now reads `progess_customer`

## [1.0.0] - 2019-08-20

-   Initial release
