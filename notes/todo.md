# To do

## Check Boolean array exposition

We have some in resampling_with_code2, and some before, but this is a hard
topic, and we should put more exposition time into it.

## Strings

## Gently work up to using `choice` with `p`

We want to get to using `choice(['foo', 'bar'], p=[0.7, 0.3])`

Start with say using random integers, or choice with the correct proportion of
inputs (`choice(['foo'] * 7 + ['bar'] * 3])`). Work up to probability, and the
`p=` form above.

## Swain jury

https://supreme.justia.com/cases/federal/us/380/202/

> Purposeful racial discrimination is not satisfactorily established by
showing only that an identifiable group has been underrepresented by as much
as 10%. P. 380 U. S. 208.

Redo simulation with proportion 0.26 * 0.9 = 0.234

## Glossary

`probability_theory_1a.Rmd` referred to a "Glossary", but in fact, the original
book does not have one, either in PDF or in the printed text.  We should do
one.
