.PHONY: deploy
deploy:
	rsync -az --delete -e ssh --safe-links . hubvan:~/fantasypl_stats

update:
	git pull
	python dl.py
	git add data/* players.current.json
	git commit -m 'updating data'
	git push
