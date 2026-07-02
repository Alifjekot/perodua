# Create traz color placeholder images using .NET
Add-Type -AssemblyName System.Drawing

$colors = @{
    'traz_electric_blue.png' = [System.Drawing.Color]::FromArgb(25, 118, 210)
    'traz_cranberry_red.png' = [System.Drawing.Color]::FromArgb(183, 28, 28)
    'traz_granite_grey.png' = [System.Drawing.Color]::FromArgb(69, 90, 100)
    'traz_glittering_silver.png' = [System.Drawing.Color]::FromArgb(192, 192, 192)
    'traz_ivory_white.png' = [System.Drawing.Color]::FromArgb(245, 240, 230)
}

Set-Location 'c:\Users\user\Downloads\akmal perodua\gambar'

foreach ($file in $colors.Keys) {
    $bitmap = New-Object System.Drawing.Bitmap(800, 600)
    $brush = New-Object System.Drawing.SolidBrush($colors[$file])
    $graphics = [System.Drawing.Graphics]::FromImage($bitmap)
    $graphics.FillRectangle($brush, 0, 0, 800, 600)
    $bitmap.Save($file)
    $graphics.Dispose()
    $brush.Dispose()
    $bitmap.Dispose()
    Write-Host "Created $file"
}

Write-Host 'All traz color images created!'
