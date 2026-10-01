# Claude's Paper Book

A $50,000 **paper-trading** portfolio of individual US stocks, run by Claude on its own. No real money, no brokerage. Every trade comes with its reasoning, an exit plan, and a result when it closes.

The goal: see whether an AI that reads the news, earnings and a few hand-picked X accounts can find the next great individual stock.

## How it works

```
 Grok (weekdays 22:15 Berlin)          reads 5 X accounts, emails an "X digest"
        │
        ▼
 Gmail ──► Claude daily review          after the US close, every trading day
             • fills yesterday's orders at today's open
             • marks the book to the close
             • checks stops, targets, earnings dates, red-flag news
             • queues orders for tomorrow's open (default: no trade)
        │
        ▼
 Claude weekly review                   Saturday morning
             • re-underwrites every holding
             • researches new ideas, incl. X digest leads and mid/small caps
             • queues orders for Monday's open
        │
        ▼
 Live page                              all-time return, positions, pending orders,
                                        trade log with reasoning, daily journal
```

## Rules

- Individual US stocks only. No ETFs, shorting, options or margin.
- Max 20% of the book in one stock. 5-15% cash normally, up to 40% while waiting on a catalyst.
- Decisions are made after the close and filled at the **next day's open**, never at a price already seen.
- At most 3 new positions per week, held at least 5 trading days unless the stop hits or the thesis breaks.
- Every position has a stop and a target from day one.
- Facts come from established sources (filings, Reuters, Bloomberg, CNBC, exchange data). X posts are leads, never reasons on their own.
- No commissions or slippage are modeled.

## Repo layout

| Path | What it is |
| --- | --- |
| `index.html` | Static version of the page. Reads `data/portfolio.json`. |
| `data/portfolio.json` | Portfolio state, all trades and daily snapshots. |
| `prompts/` | The daily, weekly and Grok prompts that run the system. |

Run locally: `npx serve .` (the page fetches the JSON, so open it through a server, not as a file).

## Disclaimer

This is an experiment, not investment advice. Paper results ignore costs, taxes and the psychology of real money.
