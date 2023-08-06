<br>
<br>
<div align='center'>

<a href="https://nilomr.github.io/pykanto">
    <img src="docs/custom/pykanto-logo-grey-04.svg" alt="pykanto logo" title="pykanto" height="80" style="padding-bottom:1em !important;" />
</a>

<br>
<br>

![version](https://img.shields.io/badge/package_version-0.1.0-orange)
![PyPI status](https://img.shields.io/pypi/status/ansicolortags.svg)
![license](https://img.shields.io/github/license/mashape/apistatus.svg)
![Open Source Love](https://img.shields.io/badge/open%20source-♡-lightgrey)
![Python 3.8](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10-blue.svg)

**pykanto** is a python library to manage and analyse bird vocalisations

[Installation](#installation) •
[Getting started](#getting-started) •
[Acknowledgements](#acknowledgements)
# ㅤ

</div>

### Installation

See [installing pykanto](https://nilomr.github.io/pykanto/contents/1_getting-started.html) for a complete installation guide.

To install pykanto using pip, simply run:
```
pip install pykanto
```
<br>

### Getting started

See [getting
started](https://nilomr.github.io/pykanto) for a
complete use guide.

<br>

### Datasets
There are three small vocalisation datasets packaged with `pykanto`, used
for unit tests and demonstration purposes. These will be downloaded automatically
when you install the library.

| Dataset                          | Description                                                  | Source                                                                                                                                                                                              |
| -------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Great tit songs                  | Dawn songs from male birds in a population in Oxford, UK     | Nilo M. Recalde                                                                                                                                                                                     |
| European storm-petrel purr songs | Males singing from burrows in the Shetland and Faroe islands | [XC46092](https://xeno-canto.org/46092) © Dougie Preston <br> [XC663885](https://xeno-canto.org/663885) © Simon S. Christiansen // [CC licence](https://creativecommons.org/licenses/by-nc-nd/2.5/) |
| Bengalese finch songs            | Recordings from two isolated Bengalese finches               | Originally published in [Tachibana, Koumura & Okanoya (2015)](https://link.springer.com/article/10.1007/s00359-015-1046-z) Data: [DOI](https://osf.io/r6paq/)                                       |

<br>

### License

The project is licensed under the [MIT license](./LICENSE).

<br>

### Citation
If you use `pykanto`, please cite the associated preprint: <br>
![DOI](https://img.shields.io/badge/DOI-coming%20soon-yellow)


<br>

### Acknowledgements

- Some of the methods that are part of `pykanto` are directly inspired by or adapted from
[Sainburg, Thielk and Gentner
(2020)](https://doi.org/10.1371/journal.pcbi.1008228). I have indicated where
this is the case in the relevant method's docstring.

- The
[`dereverberate`](https://github.com/nilomr/pykanto/blob/b11f3b59301f444f8098d76da96cc87bd9cb624b/pykanto/signal/filter.py#L14)
function is based on code by Robert Lachlan that is part of
[Luscinia](https://rflachlan.github.io/Luscinia/), a powerful software for
bioacoustic archiving, measurement and analysis.
  
- I have learnt a lot about packaging and python by perusing the structure of
projects by [NickleDave](https://github.com/NickleDave/NickleDave). I became
aware of [VocalPy](https://github.com/vocalpy), a project that aims to "_develop
an ecosystem of interoperable packages_" for "_computational vocal
communication and learning research_" when I
had already written most of `pykanto`, but eventually I'd like to make it
compatible with it: standardisation is
direly needed in the field and I don't want to contribute to the chaos.


# ㅤ
<sub>© Nilo M. Recalde, 2021-present</sub>

