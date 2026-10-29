<script lang="ts">
  import reports from '#lib/data/reports-4471.json';
  import type { Report } from '#lib/kb/causes';
  import { tenantOf } from '#lib/kb/locales';
  import { PROBLEM_TEXT, splitTicket, type Problem } from '#lib/kb/problems';

  // `tickets`: the issue each problem was filed as, by problem. `repo`: where those issues live.
  let { ticket, tickets = {}, repo }: { ticket: number; tickets?: Partial<Record<Problem, number>>; repo: string } = $props();

  const split = $derived(splitTicket(reports as Report[], ticket, tenantOf));
</script>

<p class="sum">
  <strong>{split.unique}</strong> reports merged into #{ticket} ·
  <strong>{split.groups.length}</strong>
  {split.groups.length === 1 ? 'problem' : 'problems'}, counted the desk's way
</p>

<table>
  <thead>
    <tr><th>problem</th><th>reports</th><th>tenants</th><th>seen</th><th>intake tagged otherwise</th><th>ticket</th></tr>
  </thead>
  <tbody>
    {#each split.groups as g (g.problem)}
      <tr>
        <td><code>{g.problem}</code><br /><span class="what">{PROBLEM_TEXT[g.problem]}</span></td>
        <td>{g.reports}{#if g.filedUnder.length}<br /><span class="what">also in {g.filedUnder.join(', ')}</span>{/if}</td>
        <td>{g.tenants}</td>
        <td>{g.firstSeen} → {g.lastSeen}</td>
        <td>{g.mistagged}</td>
        <td>
          {#if tickets[g.problem]}
            <a href="https://github.com/{repo}/issues/{tickets[g.problem]}">{repo}#{tickets[g.problem]}</a>
          {:else}
            <span class="none">no ticket yet</span>
          {/if}
        </td>
      </tr>
    {/each}
  </tbody>
</table>

{#each split.groups.filter((g) => g.filedUnder.length) as g (g.problem)}
  <p class="note">
    {g.reports} reports read as a <code>{g.problem}</code> move are counted where the desk files them
    (<code>{g.filedUnder.join(', ')}</code>, by tenant) and again on their own row.
  </p>
{/each}

<p class="note">
  The export holds {split.exported} rows for #{ticket}; {split.exported - split.unique} of them are the same report
  exported twice, counted once.
</p>

<style>
  .sum { font-size: 1.1rem; }
  .what, .note { color: var(--muted); font-size: 0.85em; }
  .none { color: var(--warn); font-weight: 600; }
</style>
