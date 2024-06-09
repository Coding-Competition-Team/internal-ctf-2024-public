# Libwary V2.0

Author: Reyes

> After making a horrendous libwary in php for hackac24, I decided to remake one in python.
> This time, there are credits, to ensure you can only read one book at once (don't be greedy), and ensure you can't read the flag.
> Also, I've outright disabled reading the flag this time, so it should be impossible.

**Difficulty: Very Hard**

## Solution

A race condition is present in the below code, if we send simultaneous read requests, we are able to use our 10 credits multiple times, creating multiple loans, while the `credit` field of `users` is only deducted once.

```python
requiredcredits = 1000 if value == 'flag' else 10
if user[4] < requiredcredits:
  return render_template('read.html', error="Insufficient credits, try returning a book. If you reloaded, return and read again.", size=16, theme="light")

conn = sqlite3.connect('database.db')
cur = conn.cursor()
cur.execute("SELECT credit FROM users WHERE session = ?", (session,))
credits = cur.fetchone()[0] - requiredcredits

cur.execute("UPDATE users SET credit = ? WHERE session = ?", (credits, session))
cur.execute("INSERT INTO loans (user_id, credit) VALUES (?, ?)", (user[0], requiredcredits))
conn.commit()
```

Hence, we run `solve.py` and repeatedly press `Return Loaned Books` on the page to increase our credits.

Once we have gotten sufficient credits to get the flag, we encounter the error of `Access Denied: You are not allowed to read the flag.`

Note how `for key, value in request.args.items(multi=True)` we can specify multiple params for book. To get the flag, simply visit
`/read?book=rj1&size=16&theme=light&book=flag`.

## Note
By right, to avoid easy race condition, you would have to do
```sql
UPDATE users SET credit = credit - ? WHERE session = ?
```