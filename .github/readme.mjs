import README from 'readme-components'

let template_data = {
  name: 'kerboodle-scraper',
  author: 'Sanjay Sunil',
  email: 'sanjaysunil@protonmail.com',
  description: 'Scrape any kerboodle textbook and convert into a PDF',
  long_description: 'allows you to scrape any kerboodle textbook from kerboodle.com and combine each of its pages into one PDF file.',
}

let template = new README()
template.use_premade('header', template_data);
template.use_premade('description', template_data)
template.use_component('./components/install_usage.md')
template.use_premade('license', template_data)
template.make_readme();