---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: home
title: Home
order: 1
permalink: /cdsi_nlp/
---

Hello and welcome to the website for the Winter 2023 NLP Workshops offered by McGill's Computational and Data Systems Initiative (CDSI).

# Workshop description

A description about the workshops.

# About the instructors

A description of the cool instructors.

# Workshops
<!-- TODO: Fix broken link -->
{% for workshop in site.workshops %}
  <h2>
    <a href="{{ workshop.url | absolute_url }}">
      {{ workshop.title }}
    </a>
  </h2>
{% endfor %}