---
layout: default
title: Home
---

<section class="hero">
  <div class="hero__content">
    <p class="eyebrow">{{ site.author.affiliation }}</p>
    <h1>Yangming Zhang</h1>
    <p class="lead">
      I am a Ph.D. student at Wuhan University, working on Human-AI Interaction, multimodal LLM agents, cultural intelligence, and AI for Wellbeing.
    </p>
    <p>
      My research studies how AI systems can support culturally situated human needs in emotional support, education, and digital cultural heritage. I build interactive prototypes, run user studies, and evaluate AI systems through mixed methods.
    </p>
    <div class="hero__actions" aria-label="Profile links">
      <a class="button" href="{{ site.links.scholar }}">Google Scholar</a>
      <a class="button button--secondary" href="{{ site.links.github }}">GitHub</a>
      <a class="button button--secondary" href="{{ site.links.cv | relative_url }}">Public CV</a>
    </div>
  </div>
  <figure class="hero__visual">
    <img src="{{ '/assets/img/research-map.png' | relative_url }}" alt="Abstract research map connecting interaction, agents, culture, and wellbeing">
  </figure>
</section>

<section class="section-grid">
  <div>
    <h2>Research Interests</h2>
    <ul class="interest-list">
      <li>Human-AI Interaction and human-centered evaluation</li>
      <li>Culturally grounded AI agents and multimodal LLM systems</li>
      <li>AI for Wellbeing, education, and creative support</li>
      <li>Digital cultural heritage and computational humanities</li>
    </ul>
  </div>
  <div>
    <h2>Latest News</h2>
    <div class="news-list">
      {% for item in site.data.news limit:4 %}
        <p><span>{{ item.date }}</span> <a href="{{ item.link }}">{{ item.text }}</a></p>
      {% endfor %}
    </div>
  </div>
</section>

<section>
  <div class="section-heading">
    <h2>Featured Publications</h2>
    <a href="{{ '/publications/' | relative_url }}">All publications</a>
  </div>
  {% assign featured_publications = site.data.publications | where: "featured", true %}
  {% include publication-list.html publications=featured_publications %}
</section>

<section>
  <div class="section-heading">
    <h2>Selected Projects</h2>
    <a href="{{ '/projects/' | relative_url }}">All projects</a>
  </div>
  {% assign featured_projects = site.data.projects | where: "featured", true %}
  {% include project-list.html projects=featured_projects %}
</section>
