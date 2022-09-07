## Chapter mapping

These are the mappings between the files in this (source) directory, and the
original chapters from the [second edition
website](https://resample.com/intro-text-online).  You can find basic Markdown
ports of the original second edition PDF chapters in the `unported` directory
of the repository.

See also `./_quarto.yml.template` for files making up chapters in current
built book.

| Third edition file | Second edition file(s) | Third edition chapter title |
| ------------------ | ------------------- | ---------- |
| preface_third.Rmd | N/A | Preface to the third edition |
| preface_second.Rmd | 01-Preface | Preface to the second edition |
| intro.Rmd | 02-Intro, 04-Afternote-2 | Introduction |
| monty_hall.Rmd | N/A | N/A |
| dramatizing_resampling.Rmd | 03-Afternote-1 | N/A |
| resampling_method.Rmd | 05-Chap-1 | The resampling method |
| about_technology.Rmd | N/A | Introducing Python ... |
| resampling_with_code.Rmd | N/A | Resampling with code |
| resampling_with_code2.Rmd | N/A | More resampling with code |
| what_is_probability.Rmd | 06-Chap-2, 07-Chap-3 | NA |
| probability_theory_1a.Rmd | 08-Chap-4 | NA |
| probability_theory_1b.Rmd | 09-Chap-5 | NA |
| probability_theory_2_compound.Rmd | 10-Chap-6 | NA |
| probability_theory_3.Rmd | 11-Chap-7 | NA |
| probability_theory_4_finite.Rmd | 12-Chap-8 | NA |
| sampling_variability.Rmd | 13-Chap-9 | NA |
| monte_carlo.Rmd | 14-Chap-10 | NA |
| inference_ideas.Rmd | 15-Chap-11 | NA |
| inference_intro.Rmd | 16-Chap-12 | NA |
| point_estimation.Rmd | 17-Chap-13 | NA |
| framing_questions.Rmd | 18-Chap-14 | NA |
| testing_counts_1.Rmd | 19-Chap-15 | NA |
| significance.Rmd | 20-Chap-16 | NA |
| testing_counts_2.Rmd | 21-Chap-17 | NA |
| testing_measured.Rmd | 22-Chap-18 | NA |
| testing_procedures.Rmd | 23-Chap-19 | NA |
| confidence_1.Rmd | 24-Chap-20 | NA |
| confidence_2.Rmd | 25-Chap-21 | NA |
| reliability_average.Rmd | 26-Chap-22 | NA |
| correlation_causation.Rmd | 27-Chap-23 | NA |
| how_big_sample.Rmd | 28-Chap-24 | NA |
| bayes_simulation.Rmd | 29-Chap-25 | NA |
| exercise_solutions.Rmd | 30-Exercise-sol | NA |
| acknowlegements.Rmd | acknow | NA |
| technical_note.Rmd | Technical | NA |

Initial text for this table generated using:

```
grep ed2_fname *.Rmd | grep -v _main | sed 's/:.*ed2_fname//' | sort -t ':' -k 2 -
```
