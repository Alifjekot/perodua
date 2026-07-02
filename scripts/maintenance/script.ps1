$files = Get-ChildItem -Filter *.html
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw

    $page = $file.Name

    $homeCls = "text-slate-600 hover:text-perodua font-medium"
    $carsCls = "text-slate-600 group-hover:text-perodua font-semibold flex items-center space-x-1 py-2 focus:outline-none transition-colors"
    $feedCls = "text-slate-600 hover:text-perodua font-medium"
    $aboutCls = "text-slate-600 hover:text-perodua font-medium"

    $mHomeCls = "block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50"
    $mFeedCls = "block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50"
    $mAboutCls = "block py-2 text-slate-600 hover:text-perodua font-bold border-b border-slate-50"

    if ($page -eq 'index.html') {
        $homeCls = "text-perodua font-bold border-b-2 border-perodua py-2"
        $mHomeCls = "block py-2 text-perodua font-bold border-b border-slate-50"
    } elseif ($page -eq 'feedback.html') {
        $feedCls = "text-perodua font-bold border-b-2 border-perodua py-2"
        $mFeedCls = "block py-2 text-perodua font-bold border-b border-slate-50"
    } elseif ($page -eq 'about.html') {
        $aboutCls = "text-perodua font-bold border-b-2 border-perodua py-2"
        $mAboutCls = "block py-2 text-perodua font-bold border-b border-slate-50"
    } else {
        # It's one of the car pages
        $carsCls = "text-perodua font-bold border-b-2 border-perodua flex items-center space-x-1 py-2 focus:outline-none transition-colors"
    }

    # Replace Desktop Nav
    $desktopNavPattern = '(?is)<nav class="hidden md:flex space-x-8 items-center">.*?</nav>'
    $newDesktopNav = @"
<nav class="hidden md:flex space-x-8 items-center">
                    <a href="index.html" class="$homeCls">Home</a>

                    <div class="relative group">
                        <button
                            class="$carsCls">
                            <span>Our Cars</span>
                            <i
                                class="fa-solid fa-chevron-down text-[10px] transition-transform group-hover:rotate-180"></i>
                        </button>
                        <div
                            class="absolute left-0 mt-0 w-60 bg-white border border-slate-100 rounded-xl shadow-2xl opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all duration-200 z-50 py-2">
                            <a href="alza.html"
                                class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i
                                    class="fa-solid fa-car-side mr-3 text-slate-400"></i> NEW PERODUA ALZA</a>
                            <a href="ativa.html"
                                class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i
                                    class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA ATIVA</a>
                            <a href="myvi.html"
                                class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i
                                    class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA MYVI</a>
                            <a href="aruz.html"
                                class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i
                                    class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA ARUZ</a>
                            <a href="axia.html"
                                class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i
                                    class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA AXIA</a>
                            <a href="bezza.html"
                                class="flex items-center px-4 py-2.5 text-sm font-medium text-slate-700 hover:bg-slate-50 hover:text-perodua"><i
                                    class="fa-solid fa-car-side mr-3 text-slate-400"></i> PERODUA BEZZA</a>
                        </div>
                    </div>

                    <a href="feedback.html" class="$feedCls">Feedback Customer</a>
                    <a href="about.html" class="$aboutCls">About Me</a>

                    <a href="https://wa.me/60183500631" target="_blank"
                        class="bg-emerald-500 hover:bg-emerald-600 text-white font-bold px-5 py-2.5 rounded-xl flex items-center space-x-2 shadow-sm transition">
                        <i class="fa-brands fa-whatsapp text-lg"></i> <span>018-350 0631</span>
                    </a>
                </nav>
"@

    # Replace Mobile Nav
    $mobileNavPattern = '(?is)<div id="mobile-menu".*?</div>\s*</header>'
    $newMobileNav = @"
<div id="mobile-menu" class="hidden md:hidden bg-white border-t px-4 py-5 space-y-4 shadow-xl">
            <a href="index.html" class="$mHomeCls">Home</a>
            <a href="feedback.html" class="$mFeedCls">Feedback Customer</a>
            <a href="about.html" class="$mAboutCls">About Me</a>
            <div class="text-xs text-slate-400 font-bold tracking-wider uppercase">Pilihan Model Kereta</div>
            <div class="grid grid-cols-2 gap-2">
                <a href="alza.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Alza</a>
                <a href="ativa.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Ativa</a>
                <a href="myvi.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Myvi</a>
                <a href="aruz.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Aruz</a>
                <a href="axia.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Axia</a>
                <a href="bezza.html" class="bg-slate-50 p-3 rounded-xl text-xs font-semibold text-center text-slate-700 block hover:bg-perodua hover:text-white">Bezza</a>
            </div>
            <a href="https://wa.me/60183500631" class="w-full bg-emerald-500 text-white font-bold py-3 rounded-xl flex items-center justify-center space-x-2 shadow-md">
                <i class="fa-brands fa-whatsapp text-lg"></i> <span>Hubungi Akmal</span>
            </a>
        </div>
    </header>
"@
    
    $content = $content -replace $desktopNavPattern, $newDesktopNav
    $content = $content -replace $mobileNavPattern, $newMobileNav

    Set-Content -Path $file.FullName -Value $content -NoNewline
    Write-Output "Updated $($file.Name)"
}
