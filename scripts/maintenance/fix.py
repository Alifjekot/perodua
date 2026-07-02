import os

filepath = r'c:\Users\user\Downloads\akmal perodua\index.html'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find where it broke.
# we know up to line 189 it's correct: <div class="absolute top-0 left-0 w-full h-16 bg-white" style="clip-path: polygon(0 0, 100% 0, 100% 0, 0 100%);"></div>
# And then we want to add our car section, followed by the POV banner section

# Let's find index of line 189
start_idx = -1
for i, line in enumerate(lines):
    if 'clip-path: polygon(0 0, 100% 0, 100% 0, 0 100%);' in line:
        start_idx = i
        break

end_idx = -1
for i, line in enumerate(lines):
    if '<!-- Trade In Section -->' in line:
        end_idx = i
        break

if start_idx != -1 and end_idx != -1:
    before = lines[:start_idx+1]
    after = lines[end_idx:]
    
    middle = r'''        <div class="absolute top-0 left-0 w-full h-16 bg-white opacity-50"
            style="clip-path: polygon(100% 0, 100% 0, 100% 100%, 0 0); transform: scaleY(-1);"></div>

        <div class="max-w-7xl mx-auto px-4 relative z-10 pt-4">
            <div class="text-center mb-16">
                <span class="text-[10px] font-extrabold text-gray-400 tracking-[0.2em] uppercase bg-gray-100 px-3 py-1 rounded-sm shadow-sm border border-gray-200">TRADE-IN ACCEPTED!</span>
                <h2 class="text-3xl md:text-4xl font-extrabold text-[#1e293b] mt-4 tracking-tight">Perodua Car Models</h2>
            </div>

            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 gap-x-8 gap-y-12">
                <!-- Card: AXIA -->
                <div class="bg-white rounded-[2rem] shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-slate-100 group flex flex-col relative">
                    <div class="pt-8 pb-6 px-4 bg-gradient-to-b from-slate-50 to-white relative flex justify-center items-center h-48">
                        <div class="relative z-10 w-36 h-36 bg-white rounded-full p-2 shadow-md group-hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-2 flex items-center justify-center border-4 border-slate-50">
                            <img src="gambar/axia.jpg" alt="Axia" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/100?text=Car'">
                        </div>
                    </div>
                    <div class="px-6 pt-2 pb-8 text-center flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="font-black text-brandSlate text-lg uppercase tracking-wide mb-1">PERODUA AXIA 2023</h3>
                            <div class="w-12 h-1 bg-perodua mx-auto rounded-full mb-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <p class="text-slate-700 font-bold text-[13px]">FROM - RM 22 000.00</p>
                            <p class="text-[10px] text-slate-400 font-medium mt-1 uppercase tracking-wider">OTR (without insurance)</p>
                        </div>
                        <div class="mt-6 flex flex-col gap-2 w-full max-w-[220px] mx-auto">
                            <a href="axia.html" class="w-full border-2 border-slate-200 text-slate-600 font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider hover:border-perodua hover:text-perodua transition-colors flex items-center justify-center">View Detail</a>
                            <a href="https://wa.me/60176503339" class="w-full bg-perodua hover:bg-peroduaDark text-white font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider shadow-md shadow-perodua/30 transition-colors flex items-center justify-center">Book Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card: ALZA -->
                <div class="bg-white rounded-[2rem] shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-slate-100 group flex flex-col relative">
                    <div class="pt-8 pb-6 px-4 bg-gradient-to-b from-slate-50 to-white relative flex justify-center items-center h-48">
                        <div class="relative z-10 w-36 h-36 bg-white rounded-full p-2 shadow-md group-hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-2 flex items-center justify-center border-4 border-slate-50">
                            <img src="gambar/alza.jpg" alt="Alza" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/100?text=Car'">
                        </div>
                    </div>
                    <div class="px-6 pt-2 pb-8 text-center flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="font-black text-brandSlate text-lg uppercase tracking-wide mb-1">NEW PERODUA ALZA</h3>
                            <div class="w-12 h-1 bg-perodua mx-auto rounded-full mb-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <p class="text-slate-700 font-bold text-[13px]">FROM - RM 62 500.00</p>
                            <p class="text-[10px] text-slate-400 font-medium mt-1 uppercase tracking-wider">OTR (without insurance)</p>
                        </div>
                        <div class="mt-6 flex flex-col gap-2 w-full max-w-[220px] mx-auto">
                            <a href="alza.html" class="w-full border-2 border-slate-200 text-slate-600 font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider hover:border-perodua hover:text-perodua transition-colors flex items-center justify-center">View Detail</a>
                            <a href="https://wa.me/60176503339" class="w-full bg-perodua hover:bg-peroduaDark text-white font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider shadow-md shadow-perodua/30 transition-colors flex items-center justify-center">Book Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card: ATIVA -->
                <div class="bg-white rounded-[2rem] shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-slate-100 group flex flex-col relative">
                    <div class="pt-8 pb-6 px-4 bg-gradient-to-b from-slate-50 to-white relative flex justify-center items-center h-48">
                        <div class="relative z-10 w-36 h-36 bg-white rounded-full p-2 shadow-md group-hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-2 flex items-center justify-center border-4 border-slate-50">
                            <img src="gambar/Ativa.jpg" alt="Ativa" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/100?text=Car'">
                        </div>
                    </div>
                    <div class="px-6 pt-2 pb-8 text-center flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="font-black text-brandSlate text-lg uppercase tracking-wide mb-1">PERODUA ATIVA</h3>
                            <div class="w-12 h-1 bg-perodua mx-auto rounded-full mb-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <p class="text-slate-700 font-bold text-[13px]">FROM - RM 62 500.00</p>
                            <p class="text-[10px] text-slate-400 font-medium mt-1 uppercase tracking-wider">OTR (without insurance)</p>
                        </div>
                        <div class="mt-6 flex flex-col gap-2 w-full max-w-[220px] mx-auto">
                            <a href="ativa.html" class="w-full border-2 border-slate-200 text-slate-600 font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider hover:border-perodua hover:text-perodua transition-colors flex items-center justify-center">View Detail</a>
                            <a href="https://wa.me/60176503339" class="w-full bg-perodua hover:bg-peroduaDark text-white font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider shadow-md shadow-perodua/30 transition-colors flex items-center justify-center">Book Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card: MYVI -->
                <div class="bg-white rounded-[2rem] shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-slate-100 group flex flex-col relative">
                    <div class="pt-8 pb-6 px-4 bg-gradient-to-b from-slate-50 to-white relative flex justify-center items-center h-48">
                        <div class="relative z-10 w-36 h-36 bg-white rounded-full p-2 shadow-md group-hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-2 flex items-center justify-center border-4 border-slate-50">
                            <img src="gambar/myvi.jpg" alt="Myvi" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/100?text=Car'">
                        </div>
                    </div>
                    <div class="px-6 pt-2 pb-8 text-center flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="font-black text-brandSlate text-lg uppercase tracking-wide mb-1">PERODUA MYVI</h3>
                            <div class="w-12 h-1 bg-perodua mx-auto rounded-full mb-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <p class="text-slate-700 font-bold text-[13px]">FROM - RM 46 500.00</p>
                            <p class="text-[10px] text-slate-400 font-medium mt-1 uppercase tracking-wider">OTR (without insurance)</p>
                        </div>
                        <div class="mt-6 flex flex-col gap-2 w-full max-w-[220px] mx-auto">
                            <a href="myvi.html" class="w-full border-2 border-slate-200 text-slate-600 font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider hover:border-perodua hover:text-perodua transition-colors flex items-center justify-center">View Detail</a>
                            <a href="https://wa.me/60176503339" class="w-full bg-perodua hover:bg-peroduaDark text-white font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider shadow-md shadow-perodua/30 transition-colors flex items-center justify-center">Book Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card: ARUZ -->
                <div class="bg-white rounded-[2rem] shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-slate-100 group flex flex-col relative">
                    <div class="pt-8 pb-6 px-4 bg-gradient-to-b from-slate-50 to-white relative flex justify-center items-center h-48">
                        <div class="relative z-10 w-36 h-36 bg-white rounded-full p-2 shadow-md group-hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-2 flex items-center justify-center border-4 border-slate-50">
                            <img src="gambar/aruz.jpg" alt="Aruz" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/100?text=Car'">
                        </div>
                    </div>
                    <div class="px-6 pt-2 pb-8 text-center flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="font-black text-brandSlate text-lg uppercase tracking-wide mb-1">PERODUA ARUZ</h3>
                            <div class="w-12 h-1 bg-perodua mx-auto rounded-full mb-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <p class="text-slate-700 font-bold text-[13px]">FROM - RM 72 900.00</p>
                            <p class="text-[10px] text-slate-400 font-medium mt-1 uppercase tracking-wider">OTR (without insurance)</p>
                        </div>
                        <div class="mt-6 flex flex-col gap-2 w-full max-w-[220px] mx-auto">
                            <a href="aruz.html" class="w-full border-2 border-slate-200 text-slate-600 font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider hover:border-perodua hover:text-perodua transition-colors flex items-center justify-center">View Detail</a>
                            <a href="https://wa.me/60176503339" class="w-full bg-perodua hover:bg-peroduaDark text-white font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider shadow-md shadow-perodua/30 transition-colors flex items-center justify-center">Book Now</a>
                        </div>
                    </div>
                </div>

                <!-- Card: BEZZA -->
                <div class="bg-white rounded-[2rem] shadow-lg hover:shadow-2xl transition-all duration-300 overflow-hidden border border-slate-100 group flex flex-col relative">
                    <div class="pt-8 pb-6 px-4 bg-gradient-to-b from-slate-50 to-white relative flex justify-center items-center h-48">
                        <div class="relative z-10 w-36 h-36 bg-white rounded-full p-2 shadow-md group-hover:shadow-xl transition-all duration-500 transform group-hover:-translate-y-2 flex items-center justify-center border-4 border-slate-50">
                            <img src="gambar/bezza.jpg" alt="Bezza" class="w-full h-full object-contain" onerror="this.src='https://via.placeholder.com/100?text=Car'">
                        </div>
                    </div>
                    <div class="px-6 pt-2 pb-8 text-center flex-grow flex flex-col justify-between">
                        <div>
                            <h3 class="font-black text-brandSlate text-lg uppercase tracking-wide mb-1">PERODUA BEZZA</h3>
                            <div class="w-12 h-1 bg-perodua mx-auto rounded-full mb-4 opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
                            <p class="text-slate-700 font-bold text-[13px]">FROM - RM 34 580.00</p>
                            <p class="text-[10px] text-slate-400 font-medium mt-1 uppercase tracking-wider">OTR (without insurance)</p>
                        </div>
                        <div class="mt-6 flex flex-col gap-2 w-full max-w-[220px] mx-auto">
                            <a href="bezza.html" class="w-full border-2 border-slate-200 text-slate-600 font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider hover:border-perodua hover:text-perodua transition-colors flex items-center justify-center">View Detail</a>
                            <a href="https://wa.me/60176503339" class="w-full bg-perodua hover:bg-peroduaDark text-white font-bold py-2.5 rounded-xl text-[11px] uppercase tracking-wider shadow-md shadow-perodua/30 transition-colors flex items-center justify-center">Book Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- POV Banner Section -->
    <section class="w-full bg-gradient-to-b from-[#f4f7fb] to-white relative pt-16 pb-4">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="rounded-[2rem] overflow-hidden shadow-[0_20px_50px_rgba(0,150,57,0.2)] relative group border-[8px] border-white">
                <img src="gambar/pov-banner.png" alt="Buy Quality Perodua Certified Pre-Owned Vehicles" class="w-full h-auto object-cover transform group-hover:scale-[1.03] transition-transform duration-700 ease-out" onerror="this.src='https://placehold.co/1200x300/00752c/ffffff?text=Sila+Save+Gambar+Banner+Sebagai+pov-banner.png+Dalam+Folder+gambar'">
                <div class="absolute inset-0 bg-gradient-to-t from-black/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none"></div>
                <div class="absolute inset-0 ring-1 ring-inset ring-black/10 rounded-[2rem] pointer-events-none"></div>
            </div>
        </div>
    </section>
'''

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(before)
        f.write(middle + '\n')
        f.writelines(after)
    print("Successfully replaced.")
else:
    print(f"Failed. start: {start_idx}, end: {end_idx}")


