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

<div class="page__section" style="margin-top:1.5rem">
  <div class="feature__item" style="display:flex;gap:1.25rem;align-items:center;flex-wrap:wrap">
    <img src="/images/profile.png" alt="Jiarong Guo" style="width:96px;height:96px;border-radius:50%">
    <div>
      <h2 style="margin:0 0 .25rem 0">Hi, I'm Jiarong</h2>
      <p style="margin:0">I build robust AI for medical imaging, from segmentation and reconstruction to clinically useful decision support. Currently in Hong Kong.</p>
      <p style="margin:.5rem 0 0 0"><a class="btn btn--primary" href="/about/">About me</a></p>
    </div>
  </div>
</div>

<div class="page__section" style="margin-top:2rem">
  <h2>Research interests</h2>
  <ul>
    <li>Medical image segmentation and registration</li>
    <li>Reconstruction, denoising, and image quality enhancement</li>
    <li>Self-supervised and foundation models for medical imaging</li>
    <li>Trustworthy AI: robustness, interpretability, and fairness</li>
  </ul>
</div>

<div class="page__section" style="margin-top:2rem">
  <h2>What I'm doing now</h2>
  <ul>
    <li>Building datasets and benchmarks for medical imaging tasks</li>
    <li>Training compact, deployment-ready models for clinical settings</li>
    <li>Collaborating with hospitals and labs worldwide</li>
  </ul>
</div>

<div class="page__section" style="margin-top:2rem">
  <h2>Time schedule</h2>
  <dl>
    <dt>Mon–Fri</dt><dd>09:00–18:00 HKT</dd>
    <dt>Best hours for meetings</dt><dd>14:00–17:00 HKT</dd>
    <dt>Response time</dt><dd>Within 24h on weekdays</dd>
  </dl>
</div>

<div class="page__section" style="margin-top:2rem">
  <h2>Highlights</h2>
  <div class="feature__wrapper">
    <div class="feature__item">
      <h3>Publications</h3>
      <p>Peer-reviewed papers in medical imaging and computer vision.</p>
      <p><a class="btn btn--primary" href="/publications/">View publications</a></p>
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

<div class="page__section" style="margin-top:2rem">
  <h2>Get in touch</h2>
  <p>Email: <a href="mailto:jiarong.guo01@gmail.com">jiarong.guo01@gmail.com</a> · LinkedIn: <a href="https://linkedin.com/in/jiarong-guo-4aa0181b8" target="_blank" rel="noopener">@jiarong</a> · GitHub: <a href="https://github.com/JR-Guo" target="_blank" rel="noopener">JR-Guo</a></p>
</div>

