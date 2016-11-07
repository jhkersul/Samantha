import wikipedia
import re

class SearchWiki(object):

    def get_summary(title):
        wikipedia.set_lang("pt")
        summary = wikipedia.summary(title, sentences=2)

        new_summary = SearchWiki.regexer_cleaner(summary)

        return new_summary

    def regexer_cleaner(summary):
        return re.sub(r' \(.*\)', '', summary)
