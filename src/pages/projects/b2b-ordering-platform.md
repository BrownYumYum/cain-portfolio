---
import Layout from '../../layouts/Layout.astro';
---

<Layout title="Enterprise B2B Ordering Platform | Cain Anthony Macias">
  <div class="fixed inset-0 -z-10 bg-zinc-950">
    <div class="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:32px_32px]"></div>
    <div class="absolute inset-0 bg-[radial-gradient(at_top_center,rgba(63,63,70,0.15)_0%,transparent_80%)]"></div>
  </div>

  <div class="max-w-4xl mx-auto px-6 py-12 md:py-20">
    <a href="/projects" class="text-zinc-500 hover:text-white transition-colors mb-8 inline-block">&larr; Back to Systems</a>
    
    <header class="mb-16 border-b border-zinc-800 pb-12">
      <h1 class="text-3xl md:text-5xl font-bold text-white mb-10 tracking-tight">Enterprise B2B Ordering Platform</h1>
      
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-base">
        <div class="bg-zinc-900/40 border border-zinc-800 p-6 rounded-xl">
          <h3 class="text-zinc-500 font-bold mb-3 uppercase tracking-wider text-xs">Problem</h3>
          <p class="text-zinc-300 leading-relaxed">
            Manual ordering processes created pricing errors, delays, and operational bottlenecks for institutional clients. Tiered pricing structures were especially prone to inconsistencies, requiring frequent manual corrections.
          </p>
        </div>
        
        <div class="bg-zinc-900/40 border border-zinc-800 p-6 rounded-xl">
          <h3 class="text-zinc-500 font-bold mb-3 uppercase tracking-wider text-xs">Solution</h3>
          <p class="text-zinc-300 leading-relaxed">
            Developed a full-stack Django platform that automated account-based ordering and pricing logic, eliminating manual data entry and enforcing contract-level pricing rules across all transactions.
          </p>
        </div>
        
        <div class="bg-zinc-900 border border-zinc-700 p-6 rounded-xl ring-1 ring-white/10 relative overflow-hidden">
          <div class="absolute top-0 left-0 w-1 h-full bg-white"></div>
          <h3 class="text-white font-bold mb-3 uppercase tracking-wider text-xs">Impact</h3>
          <ul class="text-zinc-200 space-y-3 font-medium">
            <li class="flex gap-2 items-start"><span class="text-zinc-500">→</span> Reduced pricing errors and manual intervention</li>
            <li class="flex gap-2 items-start"><span class="text-zinc-500">→</span> Improved order processing speed and accuracy</li>
            <li class="flex gap-2 items-start"><span class="text-zinc-500">→</span> Enabled scalable, self-service procurement workflows</li>
          </ul>
        </div>
      </div>
    </header>

    <section class="mb-16">
      <h2 class="text-2xl font-bold text-white mb-6">System Design & Implementation</h2>
      <p class="text-zinc-300 text-lg mb-8 leading-relaxed max-w-3xl">
        Built a full-stack Django application to support complex, account-based procurement workflows with automated pricing logic.
      </p>
      
      <div class="space-y-8 text-zinc-400 border-l border-zinc-800 pl-6 ml-2">
        <div class="relative">
          <div class="absolute -left-[29px] top-1.5 w-2 h-2 rounded-full bg-zinc-600"></div>
          <h4 class="text-white font-medium text-lg mb-1">Dynamic Pricing Engine</h4>
          <p class="leading-relaxed">Designed a relational database schema to support dynamic, contract-based pricing tied to customer accounts.</p>
        </div>
        
        <div class="relative">
          <div class="absolute -left-[29px] top-1.5 w-2 h-2 rounded-full bg-zinc-600"></div>
          <h4 class="text-white font-medium text-lg mb-1">Cloud Infrastructure</h4>
          <p class="leading-relaxed">Deployed the platform on AWS (EC2 + RDS) to ensure reliability, scalability, and secure data handling.</p>
        </div>
        
        <div class="relative">
          <div class="absolute -left-[29px] top-1.5 w-2 h-2 rounded-full bg-zinc-600"></div>
          <h4 class="text-white font-medium text-lg mb-1">Frontend Engineered</h4>
          <p class="leading-relaxed">Engineered the user interface to strictly align with Section 508 accessibility standards, ensuring seamless usability and compliance across all institutional client portals.</p>
        </div>
      </div>
    </section>

    <section class="bg-zinc-900/50 border border-zinc-800 rounded-2xl overflow-hidden">
      <div class="p-6 md:p-8 border-b border-zinc-800">
        <h2 class="text-xl font-bold text-white mb-2">Technical Example: Pricing Logic</h2>
        <p class="text-zinc-400 text-base">This logic ensures contract-specific pricing is automatically applied, eliminating manual adjustments and reducing pricing inconsistencies.</p>
      </div>
      <div class="p-6 md:p-8 overflow-x-auto text-sm font-mono text-zinc-300 bg-[#0d1117]">
<pre><code># Technical Proof: Tiered Pricing Logic Snippet
# This logic ensures the correct contract pricing is applied per institutional account.

class CustomerContract(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    price_level = models.IntegerField(default=1) # Maps to ERP Price Lines

    def get_custom_price(self, product):
        """
        Dynamically calculate price based on tiered contract levels
        and applying automated account-specific discounts.
        """
        discount_factor = self.price_level * 0.05
        return product.base_price * (1 - discount_factor)
</code></pre>
      </div>
    </section>
  </div>
</Layout>
