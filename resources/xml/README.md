# XML Resources

This directory contains the XML source files for Euclid's Elements.

## Structure

- `books/`: Contains the full XML for each book of the Elements.
- `grav_md/`: Contains markdown files generated from the XML.
- `images/`: Contains images used in the XML.
- `canonical_images/`: Contains canonical images for the propositions.

## Changes

- The `split/` and `test/` directories have been removed to consolidate the XML source into the `books/` directory.
- A script `find_refs.py` was created to identify proposition references within enunciations.
- The reference in the enunciation of `elem.1.22` has been moved to the proof section.
