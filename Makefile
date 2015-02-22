.PHONY: deploy
deploy:
	rsync -az --delete -e ssh --safe-links . hubvan:~/fantasypl_stats

.PHONY: update
update:
	git fetch && git reset --hard origin/master
	python dl.py
	git add data/* players.current.json
	git commit -m 'updating current players data'
	git push

.PHONY: top1k
top1k:
	python scrape_top1k.py
	git add top1k/* top1k.current.json
	git commit -m 'updating top1k data'
	git push
