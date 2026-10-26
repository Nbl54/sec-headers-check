import argparse
import sys
import requests
from rich.console import Console
from rich.table import Table

console = Console()

SECURITY_HEADERS = {
    "Strict-Transport-Security": "Zorunlu HTTPS bağlantısını güvenceye alır (HSTS).",
    "Content-Security-Policy": "XSS ve veri enjeksiyonu saldırılarını engeller (CSP).",
    "X-Frame-Options": "Clickjacking (tıklama hırsızlığı) saldırılarını engeller.",
    "X-Content-Type-Options": "MIME-sniffing açıklarını önler (nosniff).",
    "Referrer-Policy": "İsteklerle sızan referrer/kaynak URL bilgisini kısıtlar.",
    "Permissions-Policy": "Kamera, mikrofon gibi tarayıcı özelliklerine erişimi sınırlar."
}

def analyze_headers(target_url: str):
    if not target_url.startswith(("http://", "https://")):
        target_url = "https://" + target_url

    console.print(f"\n[bold blue][*][/bold blue] Taranıyor: [bold white]{target_url}[/bold white]...\n")

    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(target_url, headers=headers, timeout=(5, 5), allow_redirects=True, stream=True)
    except requests.exceptions.RequestException as error:
        console.print(f"[bold red][-] Bağlantı hatası:[/bold red] {error}")
        sys.exit(1)

    table = Table(title=f"Güvenlik Başlıkları Analiz Raporu ({response.status_code})")
    table.add_column("Başlık (Header)", style="cyan", no_wrap=True)
    table.add_column("Durum", justify="center")
    table.add_column("Açıklama", style="magenta")

    score = 0
    total = len(SECURITY_HEADERS)

    for header, desc in SECURITY_HEADERS.items():
        if header in response.headers:
            status = "[bold green]MEVCUT[/bold green]"
            score += 1
        else:
            status = "[bold red]EKSİK[/bold red]"
        
        table.add_row(header, status, desc)

    console.print(table)

    percentage = int((score / total) * 100)
    color = "green" if percentage >= 80 else "yellow" if percentage >= 50 else "red"
    console.print(f"\n[bold]Güvenlik Skoru:[/bold] [{color}]{score}/{total} (%{percentage})[/{color}]\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Hafif HTTP Güvenlik Başlığı Denetleyici")
    parser.add_argument("-u", "--url", required=True, help="Taranacak hedef URL (örn: github.com)")
    args = parser.parse_args()

    analyze_headers(args.url)
