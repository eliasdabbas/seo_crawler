# SEO Crawler
Bare-bones Basic SEO Crawler using Python Scrapy

Using Scrapy, get the main SEO elements for exploratory analysis of a website. 
It works by supplying a list of known URLs to crawl and return structured results. 

The main elements include: 
- url: the actual URL 
- slug: the URI part of the URL
- directories: splits the URI by slashes to return the different folders (directories) in each URI
- title: the <title> tag
- h1, h2, h3, h4: <h> header tags
- description: the meta description
- link_urls: not activated, needs special configuration to make sure you are getting links to certain sites
- link_text: depends on the above, extracts the anchor text of each link
- link_count: number of links on page (based on your criteria)
- load_time: page load time in seconds
- status_code: response code of page 200, 301, 404, etc. 

Many other elements should be added to the list but they differ from site to site, some examples: 

- publishing date
- product price
- content category
- tags of an article
- whether or not a certain keyword is in a certain location
- type of content (inferred from a URL directory, or from certain content on page) 
- etc. 
