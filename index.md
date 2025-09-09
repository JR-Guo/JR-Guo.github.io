---
layout: splash
permalink: /
title: "Jiarong Guo — Medical Image Analysis & Computer Vision"
excerpt: "AI for Healthcare • Medical Imaging • Computer Vision"
header:
  overlay_image: /images/image-alignment-1200x4002.jpg
  overlay_filter: 0.35
  actions:
    - label: "View Publications"
      url: "/publications/"
    - label: "Contact Me"
      url: "mailto:jiarong.guo01@gmail.com"
intro:
  - image_path: /images/profile.png
    title: "Hi, I'm Jiarong"
    excerpt: "I build robust AI for medical imaging, from segmentation and reconstruction to clinically useful decision support. Currently in Hong Kong."
    btn_label: "About me"
    url: "/about/"
highlights:
  - title: "Research Interests"
    items:
      - "Medical Image Segmentation and Registration"
      - "Reconstruction, Denoising, and Image Quality Enhancement"
      - "Self-supervised and Foundation Models for Medical Imaging"
      - "Trustworthy AI: robustness, interpretability, and fairness"
  - title: "What I'm Doing Now"
    items:
      - "Building datasets and benchmarks for medical imaging tasks"
      - "Training compact, deployment-ready models for clinical settings"
      - "Collaborating with hospitals and labs worldwide"
schedule:
  - title: "Time Schedule"
    note: "Available for collaborations and talks"
    slots:
      - label: "Mon–Fri"
        value: "09:00–18:00 HKT"
      - label: "Best hours for meetings"
        value: "14:00–17:00 HKT"
      - label: "Response time"
        value: "Within 24h on weekdays"
blog_preview:
  title: "Latest from the blog"
---

{% include author-profile.html %}

<div class="page__section" style="margin-top:2rem">
  <h2>Highlights</h2>
  <div class="feature__wrapper">
    <div class="feature__item">
      <h3>Publications</h3>
      <p>Peer-reviewed papers in medical imaging and computer vision.</p>
      <p><a class="btn btn--primary" href="/publications/">View publications</a></p>
    </div>
    <div class="feature__item">
      <h3>Talks</h3>
      <p>Invited talks and conference presentations.</p>
      <p><a class="btn" href="/talks/">See talks</a></p>
    </div>
    <div class="feature__item">
      <h3>Global map</h3>
      <p>Research collaborators and venues around the world.</p>
      <p><a class="btn" href="/global-map/">Explore map</a></p>
    </div>
  </div>
</div>

<div class="page__section" style="margin-top:2rem">
  <h2>Latest from the blog</h2>
  <div>
    {%- assign recent_posts = site.posts | where_exp: "post", "post.draft != true" | sort: "date" | reverse -%}
    {%- for post in recent_posts limit:3 -%}
      <article class="archive__item" style="margin-bottom:1rem">
        <h3 class="archive__item-title" style="margin:0"><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3>
        <p class="page__meta" style="margin:.25rem 0 0 0">{{ post.date | date: "%b %d, %Y" }} · {% include read-time.html %}</p>
        {%- if post.excerpt -%}
          <p style="margin:.25rem 0 0 0">{{ post.excerpt | strip_html | truncate: 140 }}</p>
        {%- endif -%}
      </article>
    {%- endfor -%}
  </div>
  <p><a class="btn" href="/year-archive/">Read all posts</a></p>
</div>

