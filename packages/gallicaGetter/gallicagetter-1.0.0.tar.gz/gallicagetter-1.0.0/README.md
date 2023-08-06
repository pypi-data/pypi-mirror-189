# gallicaGetter

This tool wraps a few endpoints from the [Gallica API](https://api.bnf.fr/api-gallica-de-recherche).

Current functionality:
* context for term occurrence and page numbers
* for a term, all the volumes the term appears in 
* for a term, the number of volumes with >= 1 occurrence over a range (per year, per month)
* full text for a volume on Gallica
* paper titles and publishing range data
* years published for a paper (used internally in papers)

I developed this tool into a [graphing app](https://www.gallicagrapher.com/) similar to Google's n-gram viewer for books. There is much more metadata in the Gallica API response I don't currently parse. Happy to add more; pull requests are also welcome! 

For an exact number of occurrences over a period, normalized by total words in that period, use [Pyllicagram](https://github.com/regicid/pyllicagram).

# Installation

```sh
pip install gallicaGetter
```
# Production Example

Here's a snippet of code from my API that makes use of the volume and context wrappers.

```python
from gallicaGetter import wrapperFactory as wF

# fetch the volumes in which terms appear
volume_Gallica_wrapper = wF.WrapperFactory.volume()
gallica_records = volume_Gallica_wrapper.get(
    terms=terms,
    start_date=make_date_from_year_mon_day(year, month, day),
    codes=codes,
    source=source,
    link=link,
    num_results=limit,
    start_index=cursor,
    sort=sort,
    on_get_total_records=set_total_records,
)

# fetch the context for those terms
content_wrapper = wF.WrapperFactory.context()
keyed_records = {record.url.split("/")[-1]: record for record in gallica_records}
context = content_wrapper.get(
    [
        (record.url.split("/")[-1], record.term)
        for _, record in keyed_records.items()
    ]
)

# combine the two
records_with_context: List[GallicaRecord] = []
for record in context:
    corresponding_record = keyed_records[record.ark]
    records_with_context.append(
        (
            corresponding_record.paper_title,
            corresponding_record.paper_code,
            corresponding_record.term,
            str(corresponding_record.date),
            corresponding_record.url,
            record,
        )
    )
print(records_with_contex)
```


