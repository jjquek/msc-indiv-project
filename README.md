# MSc Computing (Imperial College, London) Individual Project

**TL;DR** -- inspect this repository if:
* you want to see some work I did for my Master's project
* you want to see some Python code I wrote
* you want to learn about an uP-and-CoMing, blEEdIng-edGe technology: Federated Analytics.

**Table of Contents**
- [MSc Computing (Imperial College, London) Individual Project](#msc-computing-imperial-college-london-individual-project)
  - [Overview](#overview)
  - [Project Area : Federated Analytics](#project-area--federated-analytics)
  - [Repository Contents :](#repository-contents-)
    - [`dp-experiments`](#dp-experiments)
    - [`safe-experiments`](#safe-experiments)
  - [Project Takeaways :](#project-takeaways-)

## Overview

This repository contains key files from my **individual research project** done for my MSc Computing degree at Imperial College, London. It includes both `.pdf`s of the Jupyter notebooks I submitted, along with **Python scripts** I wrote for the notebooks. I have also included the `final_report.pdf` which I had submitted.

Here, I provide context on what the project was about, and what my main takeaways were.

## Project Area : Federated Analytics

This research project focused on evaluating the applicability of protocols in *Federated Analytics* to software projects. The aim was proof-of-concept, so the project focused on evaluating their applicability to a hypothetical use case, which is described in the first chapter of the `final_report`. 

**Federated Analytics** is a kind of data science. The aim is to allow analysts to compute statistical functions on population data that is hidden from them. The consequence is that data analysis can be done on user data without comprimising user privacy. 

<div style="width:100%;height:0;padding-bottom:72%;position:relative;"><iframe src="https://giphy.com/embed/oYtVHSxngR3lC" width="100%" height="100%" style="position:absolute" frameBorder="0" class="giphy-embed" allowFullScreen></iframe></div><p><a href="https://giphy.com/gifs/mfw-everything-reddit-oYtVHSxngR3lC">via GIPHY</a></p>

Various protocols have been developed and employed by companies like [Google](https://ai.googleblog.com/2020/05/federated-analytics-collaborative-data.html) and [Microsoft](https://www.microsoft.com/en-us/research/blog/collecting-telemetry-data-privately/).

In my project, I focus on evaluating two kinds of protocols: *differentially private* protocols and *Bayesian Federated Analytic* protocols. 

A decent explanation of these protocols would bloat this `README` beyond readibility, so I direct interested persons to the `final_report` for the goods.  

## Repository Contents :

The two main directories are `dp-experiments` and `safe-experiments`. 

### `dp-experiments` 

This directory includes:
* `model-for-epislon.pdf`-- a PDF of a notebook containing a partial implementation of the model proposed by [Hsu et al.](https://ieeexplore.ieee.org/document/6957125) for determining appropriate parameter values for differentially private mechanisms.
* `model-for-dp.py` which simply implements their model as Python functions within a class.

The contents of this directory is relatively little compared to `safe-experiments` because I mainly focus on evaluating the **SAFE** protocol, for reasons I discuss in my `final_report`.

### `safe-experiments`

`safe` is the acronym for the **S**ecure **A**ggregation of **F**eature **V**ector protocol proposed by [Huth and Chualwar](https://arxiv.org/abs/2107.13640). As it's name suggests, it allows an analyst to securely aggregate feature vectors (submitted by users). 

This directory includes several `.pdf` files, which should be read in the following order:
1. `safe-illustration`-- explains and illustrates the application of the SAFE protocol
2. `safe-applied-to-use-case`-- illustrates how it could be applied to the hypothetical use case I am concerned with in the project
3. `random-D-safe-run`-- illustrates the application of the extended SAFE protocol I suggest in Chapter 4 of the `final_report`. The basic idea was to make the SAFE protocol more secure by randomizing a key parameter value, effectively limiting information flow for analysts. 

The `MoodAppUser.py` and `secure_SAFE_utils.py` scripts are hopefully sufficiently well-documented to be understood on their own. Their code is used in the notebooks.

## Project Takeaways :

I found this project very challenging and intimidating because of how unfamiliar all the domains involved were to me. 

Through the work I did for this project, I'd say I've learnt the following:
* how to tackle unfamiliar problem spaces and devise solutions
* how to tolerate and get a handle on lots of scary math


