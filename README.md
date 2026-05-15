# cs50-i18n

Open multilingual version of CS50 Harvard course materials. The theme matches the original site at https://cs50.harvard.edu/x/ and the content is available in English, Vietnamese, and Chinese.

Live at https://cs50.tamnd.com (Cloudflare) and https://tamnd.github.io/cs50-i18n (GitHub Pages).

## Languages

| Language | Status |
|----------|--------|
| English | Full (all weeks, problem sets, problems) |
| Vietnamese | Week 0 translated, rest in progress |
| Chinese | Week 0 translated, rest in progress |

## Structure

```
content/
  en/x/      English content (seeded from cs50.harvard.edu)
  vi/x/      Vietnamese translations
  zh/x/      Chinese translations
themes/cs50/ Hugo theme matching the CS50 site design
```

## Run locally

```bash
hugo server -D
```

Open http://localhost:1313 in your browser.

## Build

```bash
hugo --minify
```

Output goes to `public/`.

## Contribute

Translations are welcome. Pick a week or problem set from `content/en/x/` and create the equivalent file under `content/vi/x/` or `content/zh/x/` with the translation as the body text. Keep the frontmatter and add `translatedBy: "Your Name"`.

## License

CC BY-NC-SA 4.0. See [LICENSE](LICENSE) for full terms.

Original CS50 course content is copyright 2024 Harvard University. CS50 is a registered trademark of Harvard University.
