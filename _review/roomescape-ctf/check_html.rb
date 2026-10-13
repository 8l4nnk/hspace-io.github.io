# Run from the repository root after building with --drafts.
require "html-proofer"

root = File.expand_path("_site-review")
[1, 3].each do |part|
  page = File.join(root, "posts", "roomescape-ctf-part-#{part}", "index.html")
  # The upstream theme references a manifest that is absent from the repository.
  # Keep this single known site-wide defect separate from the draft checks.
  HTMLProofer.check_file(
    page,
    root_dir: root,
    disable_external: true,
    ignore_urls: ["/assets/img/favicons/site.webmanifest"]
  ).run
end
