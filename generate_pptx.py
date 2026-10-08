import os
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # completely blank layout

    # Color definitions
    BG_COLOR = RGBColor(11, 15, 25)         # #0B0F19
    SURFACE_COLOR = RGBColor(23, 31, 51)    # #171F33
    SURFACE_ALT = RGBColor(30, 41, 67)      # #1E2943
    BORDER_COLOR = RGBColor(46, 60, 92)     # #2E3C5C
    
    ACCENT_ORANGE = RGBColor(238, 77, 45)   # #EE4D2D Shopee Orange
    ACCENT_LIGHT_ORANGE = RGBColor(255, 122, 69) # #FF7A45
    TEXT_WHITE = RGBColor(248, 250, 252)    # #F8FAFC
    TEXT_MUTED = RGBColor(154, 164, 178)    # #9AA4B2
    TEXT_DIM = RGBColor(100, 116, 139)      # #64748B
    
    GREEN = RGBColor(16, 185, 129)          # #10B981
    BLUE = RGBColor(2, 132, 199)            # #0284C7
    YELLOW = RGBColor(245, 158, 11)         # #F59E0B
    RED = RGBColor(239, 68, 68)             # #EF4444
    PURPLE = RGBColor(168, 85, 247)         # #A855F7

    FONT_MAIN = 'Arial'

    def set_slide_background(slide):
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = BG_COLOR

    def add_header(slide, kicker_text, headline_text):
        # Header Box
        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(1.1))
        tf = txBox.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        # Kicker
        p_kicker = tf.paragraphs[0]
        p_kicker.text = kicker_text.upper()
        p_kicker.font.name = FONT_MAIN
        p_kicker.font.size = Pt(11)
        p_kicker.font.bold = True
        p_kicker.font.color.rgb = ACCENT_ORANGE
        p_kicker.alignment = PP_ALIGN.LEFT
        p_kicker.space_after = Pt(4)

        # Headline
        p_head = tf.add_paragraph()
        p_head.text = headline_text
        p_head.font.name = FONT_MAIN
        p_head.font.size = Pt(22)
        p_head.font.bold = True
        p_head.font.color.rgb = TEXT_WHITE
        p_head.alignment = PP_ALIGN.LEFT

    def set_notes(slide, notes_text):
        if notes_text:
            notes_slide = slide.notes_slide
            tf = notes_slide.notes_text_frame
            tf.text = notes_text

    # -------------------------------------------------------------
    # SLIDE 1: COVER
    # -------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    
    # Ambient decorative glow card
    glow = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9))
    glow.fill.solid()
    glow.fill.fore_color.rgb = RGBColor(16, 22, 36)
    glow.line.color.rgb = RGBColor(38, 50, 77)
    glow.line.width = Pt(1.5)

    # Orange top accent line
    top_bar = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.08))
    top_bar.fill.solid()
    top_bar.fill.fore_color.rgb = ACCENT_ORANGE
    top_bar.line.fill.background()

    # Cover text
    txBox = slide1.shapes.add_textbox(Inches(1.5), Inches(1.6), Inches(10.333), Inches(4.3))
    tf = txBox.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

    p_k = tf.paragraphs[0]
    p_k.text = "TUGAS SISTEM INFORMASI  •  FORMAT TABEL ANALISIS"
    p_k.font.name = FONT_MAIN
    p_k.font.size = Pt(13)
    p_k.font.bold = True
    p_k.font.color.rgb = ACCENT_ORANGE
    p_k.space_after = Pt(18)

    p_t = tf.add_paragraph()
    p_t.text = "Tabel Analisis Sistem Informasi Shopee"
    p_t.font.name = FONT_MAIN
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.space_after = Pt(16)

    p_s = tf.add_paragraph()
    p_s.text = "Penyajian Terstruktur: Tabel Analisis IPO 4 Pilar, Tabel 6 Prinsip Perancangan SI,\nTaksonomi Jenis SI, & Evaluasi Arsitektur."
    p_s.font.name = FONT_MAIN
    p_s.font.size = Pt(17)
    p_s.font.color.rgb = TEXT_MUTED
    p_s.space_after = Pt(40)

    p_f = tf.add_paragraph()
    p_f.text = "Presentasi Individu 15 Menit  •  Program Studi Sistem Informasi"
    p_f.font.name = FONT_MAIN
    p_f.font.size = Pt(13)
    p_f.font.bold = True
    p_f.font.color.rgb = RGBColor(148, 163, 184)

    set_notes(slide1, "Selamat pagi/siang Bapak/Ibu dosen penguji serta rekan-rekan sekalian. Pada presentasi 15 menit hari ini, saya akan menyajikan tugas analisis Sistem Informasi Shopee yang disusun secara terstruktur dalam bentuk Tabel Analisis Akademik, mencakup Model IPO, 6 Prinsip Perancangan SI, Klasifikasi Sistem, hingga Evaluasi Arsitekturnya.")

    # -------------------------------------------------------------
    # SLIDE 2: AGENDA
    # -------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "Struktur Tugas (Format Tabel Analisis)", "Daftar Tabel Analisis Pembahasan")

    agenda_items = [
        ("01", "Tabel 1: Analisis Model Input – Proses – Output (IPO)", "4 Pilar Ekosistem Shopee"),
        ("02", "Landasan Teori: Enam Komponen Sistem Informasi", "Slide Perkuliahan & Studi Kasus Shopee"),
        ("03", "Tabel 2: Analisis 6 Prinsip Perancangan Sistem Informasi", "Sesuai Slide Teori Perkuliahan"),
        ("04", "Tabel 3: Analisis Klasifikasi Jenis Sistem Informasi", "TPS, MIS, DSS, & IOS Beserta Alasannya"),
        ("05", "Tabel 4: Analisis Evaluasi Perancangan Sistem", "Kelebihan, Bloatware, & Solusi Rekayasa SI"),
        ("06", "Validasi Faktual & Media Demonstrasi (Q&A)", "Rujukan Resmi, Video, & Diskusi"),
    ]

    top_y = 1.6
    for num, title, hint in agenda_items:
        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(top_y), Inches(11.733), Inches(0.78))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE_COLOR
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)

        # Text in card
        tx = slide2.shapes.add_textbox(Inches(1.1), Inches(top_y + 0.12), Inches(11.133), Inches(0.55))
        tf = tx.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        
        p = tf.paragraphs[0]
        # Number run
        r1 = p.add_run()
        r1.text = f"{num}   "
        r1.font.bold = True
        r1.font.size = Pt(14)
        r1.font.color.rgb = ACCENT_ORANGE
        
        # Title run
        r2 = p.add_run()
        r2.text = f"{title}   "
        r2.font.bold = True
        r2.font.size = Pt(14)
        r2.font.color.rgb = TEXT_WHITE

        # Hint run
        r3 = p.add_run()
        r3.text = f"—  {hint}"
        r3.font.size = Pt(12)
        r3.font.color.rgb = TEXT_MUTED

        top_y += 0.88

    set_notes(slide2, "Seluruh materi tugas ini telah saya sesuaikan ke dalam format matriks tabel analisis: Dimulai dari Tabel Analisis IPO lintas 4 pilar ekosistem, Landasan Teori Enam Komponen SI dari perkuliahan, dilanjutkan Tabel Analisis 6 Prinsip Perancangan SI sesuai materi kuliah, Tabel Klasifikasi Taksonomi SI, dan ditutup dengan Tabel Evaluasi Kritis Kelebihan, Kelemahan, serta Rekomendasi Solusinya.")

    # -------------------------------------------------------------
    # Helper to style tables
    # -------------------------------------------------------------
    def style_table(table, col_widths, headers, rows_data):
        for col_idx, width in enumerate(col_widths):
            table.columns[col_idx].width = width

        # Headers
        for col_idx, h_text in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.text = h_text
            cell.fill.solid()
            cell.fill.fore_color.rgb = RGBColor(28, 38, 61)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            for p in cell.text_frame.paragraphs:
                p.alignment = PP_ALIGN.LEFT
                p.font.name = FONT_MAIN
                p.font.bold = True
                p.font.size = Pt(10.5)
                p.font.color.rgb = ACCENT_LIGHT_ORANGE

        # Rows
        for row_idx, row_data in enumerate(rows_data):
            for col_idx, cell_data in enumerate(row_data):
                cell = table.cell(row_idx + 1, col_idx)
                cell.fill.solid()
                cell.fill.fore_color.rgb = SURFACE_COLOR if row_idx % 2 == 0 else SURFACE_ALT
                cell.vertical_anchor = MSO_ANCHOR.MIDDLE
                cell.text = "" # clear default
                tf = cell.text_frame
                tf.word_wrap = True
                tf.margin_left = Inches(0.08)
                tf.margin_right = Inches(0.08)
                tf.margin_top = Inches(0.06)
                tf.margin_bottom = Inches(0.06)

                lines = cell_data.split('\n')
                for l_idx, line in enumerate(lines):
                    p = tf.paragraphs[0] if l_idx == 0 else tf.add_paragraph()
                    p.text = line
                    p.font.name = FONT_MAIN
                    p.font.size = Pt(9.5)
                    
                    if col_idx == 0:
                        p.font.bold = True
                        p.font.color.rgb = TEXT_WHITE
                    elif col_idx == len(row_data) - 1:
                        p.font.bold = True
                        p.font.color.rgb = ACCENT_ORANGE
                    else:
                        p.font.color.rgb = TEXT_WHITE if line.startswith('•') else TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 3: TABEL 1 - ANALISIS MODEL IPO (4 PILAR)
    # -------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "Tabel Analisis 1 · Siklus Input – Proses – Output (IPO)", "Matriks Analisis IPO pada 4 Pilar Ekosistem Shopee")

    headers3 = ["Pilar / Entitas Sistem", "📥 Input (Masukan)", "⚙️ Proses (Logika Bisnis)", "📤 Output (Keluaran)", "Fitur Terkait"]
    data3 = [
        [
            "1. Sisi Pembeli\n(Buyer)",
            "• Barang keranjang (cart)\n• Alamat & titik GPS\n• Opsi bayar & voucher",
            "• Validasi 2FA / OTP\n• Garansi Shopee (Escrow)\n• Kunci kuota stok real-time",
            "• Resi otomatis & e-invoice\n• Peta live tracking kurir\n• Notifikasi status paket",
            "Checkout &\nSPX Tracking"
        ],
        [
            "2. Sisi Penjual\n(Merchant)",
            "• Master SKU & stok riil\n• Foto produk & harga\n• Balasan chat pembeli",
            "• Index algoritma pencarian\n• Potongan komisi Shopee\n• Poin penalti keterlambatan",
            "• PDF Shipping Label resi\n• Pencairan Saldo Penjual\n• Laporan omzet & performa",
            "Shopee Seller\nCentre"
        ],
        [
            "3. Sisi FinTech\n(SPayLater)",
            "• Foto e-KTP & selfie wajah\n• Kontak darurat & gaji\n• Pengajuan limit kredit",
            "• AI Credit Scoring engine\n• Pengecekan histori SLIK OJK\n• Deteksi anti-fraud & bunga",
            "• Saldo limit cicilan aktif\n• Persetujuan transaksi\n• Billing statement bulanan",
            "SPayLater &\nShopeePay"
        ],
        [
            "4. Sisi Logistik\n(SPX)",
            "• Scan barcode resi di hub\n• GPS kurir pengantar\n• Foto penerimaan paket",
            "• Algoritma optimasi rute\n• Klasterisasi wilayah antar\n• Estimasi waktu tiba (ETA)",
            "• Foto bukti kirim (POD)\n• Status paket \"Terkirim\"\n• Update riwayat lacak resi",
            "Shopee Xpress\nDriver"
        ]
    ]

    widths3 = [Inches(2.0), Inches(2.7), Inches(2.7), Inches(2.7), Inches(1.633)]
    table_shape3 = slide3.shapes.add_table(5, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    style_table(table_shape3.table, widths3, headers3, data3)

    set_notes(slide3, "Tabel pertama adalah Tabel Analisis IPO pada 4 pilar ekosistem Shopee: Pilar Pembeli menerima input keranjang dan bayar, diproses lewat Garansi Shopee dan verifikasi OTP, menghasilkan invoice dan live tracking kurir. Pilar Penjual menerima katalog produk, diproses kalkulasi komisi dan SEO, menghasilkan label resi dan saldo toko. Pilar FinTech SPayLater memproses KTP dan credit scoring, menghasilkan limit kredit. Pilar Logistik SPX memproses scan resi dan optimasi rute kurir, menghasilkan bukti serah terima paket.")

    # -------------------------------------------------------------
    # SLIDE 4: BUKTI VISUAL
    # -------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "Lampiran Visual · Pembuktian Alur IPO", "Tangkapan Layar Nyata Alur IPO Belanja di Shopee")

    card_data4 = [
        {
            "tag": "1. INPUT",
            "tag_color": ACCENT_ORANGE,
            "title": "Halaman Checkout & Cart",
            "desc": "Input data barang di keranjang belanja, pemilihan kupon voucher diskon, dan titik koordinat GPS alamat pengiriman.",
            "img": "shopee_input.jpg"
        },
        {
            "tag": "2. PROSES",
            "tag_color": BLUE,
            "title": "Garansi Shopee (Escrow Lock)",
            "desc": "Pemrosesan rekening bersama penahan dana aman, verifikasi keamanan PIN/OTP, dan penguncian stok toko real-time.",
            "img": "shopee_process.jpg"
        },
        {
            "tag": "3. OUTPUT",
            "tag_color": GREEN,
            "title": "Live Tracking Peta & Resi",
            "desc": "Keluaran nomor resi pengiriman otomatis, dokumen e-invoice, serta pergerakan kurir SPX secara langsung di peta GPS.",
            "img": "shopee_output.jpg"
        }
    ]

    card_w = Inches(3.75)
    card_gap = Inches(0.24)
    start_x = Inches(0.8)
    base_dir = os.path.join(os.getcwd(), "bolt-slides-main", "public", "images")

    for i, c in enumerate(card_data4):
        cx = start_x + i * (card_w + card_gap)
        
        # Outer Card
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, Inches(1.6), card_w, Inches(5.3))
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE_COLOR
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)

        # Image
        img_path = os.path.join(base_dir, c["img"])
        if os.path.exists(img_path):
            slide4.shapes.add_picture(img_path, cx + Inches(0.18), Inches(1.8), Inches(3.39), Inches(2.6))

        # Tag
        tag = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.25), Inches(1.9), Inches(1.2), Inches(0.35))
        tag.fill.solid()
        tag.fill.fore_color.rgb = c["tag_color"]
        tag.line.fill.background()
        tf_t = tag.text_frame
        tf_t.text = c["tag"]
        tf_t.paragraphs[0].font.name = FONT_MAIN
        tf_t.paragraphs[0].font.size = Pt(10)
        tf_t.paragraphs[0].font.bold = True
        tf_t.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
        tf_t.paragraphs[0].alignment = PP_ALIGN.CENTER

        # Title & Description
        tx_box = slide4.shapes.add_textbox(cx + Inches(0.18), Inches(4.55), Inches(3.39), Inches(2.2))
        tf_b = tx_box.text_frame
        tf_b.word_wrap = True
        tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0

        p1 = tf_b.paragraphs[0]
        p1.text = c["title"]
        p1.font.name = FONT_MAIN
        p1.font.bold = True
        p1.font.size = Pt(14)
        p1.font.color.rgb = TEXT_WHITE
        p1.space_after = Pt(8)

        p2 = tf_b.add_paragraph()
        p2.text = c["desc"]
        p2.font.name = FONT_MAIN
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

    set_notes(slide4, "Untuk melengkapi tabel analisis IPO tadi, di slide ini saya lampirkan bukti visual nyata dari aplikasi Shopee: Gambar pertama membuktikan Input di halaman Checkout saat memilih barang dan alamat. Gambar kedua membuktikan Proses sistem Garansi Shopee di mana pembayaran ditahan di rekening penampung. Gambar ketiga membuktikan Output peta pelacakan posisi kurir SPX secara live.")

    # -------------------------------------------------------------
    # SLIDE 5: LANDASAN TEORI - ENAM KOMPONEN SISTEM INFORMASI
    # -------------------------------------------------------------
    slide_komponen = prs.slides.add_slide(blank_layout)
    set_slide_background(slide_komponen)
    add_header(slide_komponen, "Materi Teori Perkuliahan · Sistem Informasi", "Enam Komponen Sistem Informasi: Teori & Studi Kasus Shopee")

    # Left card: Lecture Photo & Lecturer Key Note
    card_k_left = slide_komponen.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), Inches(3.8), Inches(5.3))
    card_k_left.fill.solid()
    card_k_left.fill.fore_color.rgb = SURFACE_COLOR
    card_k_left.line.color.rgb = BORDER_COLOR
    card_k_left.line.width = Pt(1)

    # Insert Photo if exists
    img_komponen = os.path.join(base_dir, "enam_komponen_si.jpeg")
    if not os.path.exists(img_komponen):
        img_komponen = os.path.join(os.getcwd(), "bolt-slides-main", "vidio", "WhatsApp Image 2026-10-08 at 10.41.41.jpeg")
    if os.path.exists(img_komponen):
        slide_komponen.shapes.add_picture(img_komponen, Inches(1.0), Inches(1.8), Inches(3.4), Inches(2.35))

    # Photo subtitle
    tx_sub = slide_komponen.shapes.add_textbox(Inches(1.0), Inches(4.25), Inches(3.4), Inches(0.35))
    tf_sub = tx_sub.text_frame
    tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = "Dokumentasi Slide Kuliah (SIAKAD)"
    p_sub.font.name = FONT_MAIN
    p_sub.font.size = Pt(10)
    p_sub.font.bold = True
    p_sub.font.color.rgb = ACCENT_ORANGE
    p_sub.alignment = PP_ALIGN.CENTER

    # Lecturer Quote Box
    box_quote = slide_komponen.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(4.7), Inches(3.4), Inches(1.95))
    box_quote.fill.solid()
    box_quote.fill.fore_color.rgb = RGBColor(38, 22, 22)
    box_quote.line.color.rgb = ACCENT_ORANGE
    box_quote.line.width = Pt(1)

    tf_q = box_quote.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = Inches(0.12)
    tf_q.margin_right = Inches(0.12)
    tf_q.margin_top = Inches(0.1)
    tf_q.margin_bottom = Inches(0.1)

    p_qh = tf_q.paragraphs[0]
    p_qh.text = "💡 Catatan Kunci Dosen:"
    p_qh.font.name = FONT_MAIN
    p_qh.font.bold = True
    p_qh.font.size = Pt(10)
    p_qh.font.color.rgb = ACCENT_ORANGE
    p_qh.space_after = Pt(4)

    p_qc = tf_q.add_paragraph()
    p_qc.text = "\"Manusia sering menentukan berhasil atau tidaknya SI: Sistem sebagus apa pun gagal jika tidak dipakai.\""
    p_qc.font.name = FONT_MAIN
    p_qc.font.italic = True
    p_qc.font.size = Pt(9.5)
    p_qc.font.color.rgb = TEXT_WHITE

    # Right side: Comparison Table directly for Shopee
    table_k_shape = slide_komponen.shapes.add_table(7, 3, Inches(4.8), Inches(1.6), Inches(7.733), Inches(5.3))
    table_k = table_k_shape.table
    col_w_k = [Inches(1.8), Inches(3.0), Inches(2.933)]
    headers_k = ["Komponen SI", "Penerapan Konkret pada Shopee", "Peran & Fungsi dalam Ekosistem"]
    data_k = [
        ["1. Perangkat Keras\n(Hardware)", "• Cloud Server AWS & Tencent\n• Smartphone pengguna (iOS/Android)\n• Scanner PDA & printer label SPX", "Menopang beban komputasi jutaan req/dtk, UI aplikasi mobile, serta sorting paket fisik."],
        ["2. Perangkat Lunak\n(Software)", "• Mobile App & Web Seller Centre\n• Microservices backend (Go & Java)\n• Distributed TiDB & in-memory Redis", "Menjalankan logika bisnis cart, promo flash sale, serta pembacaan data super cepat (<100ms)."],
        ["3. Data", "• Master katalog SKU & variasi harga\n• Log transaksi order & escrow lock\n• Titik GPS kurir & scoring SPayLater", "Single Source of Truth stok toko riil, pelacakan live paket, dan analisa kelayakan kredit."],
        ["4. Jaringan\n(Network)", "• Internet seluler 4G/5G publik\n• Cloudflare CDN & proteksi Anti-DDoS\n• Secure API Gateway antarlayanan", "Menghubungkan user ke server, mempercepat loading aset media, serta integrasi gateway bank."],
        ["5. Prosedur\n(Procedures)", "• SOP Garansi Shopee (Escrow)\n• SLA batas kirim seller (maks. 2 hari)\n• SOP KYC e-KTP & alur retur barang", "Menjamin keamanan dana transaksi, mencegah fraud seller-buyer, serta standardisasi servis."],
        ["6. Manusia\n(People - Kunci)", "• Pembeli (Buyer) & Merchant UMKM\n• Mitra Driver SPX & staf sortation\n• Software Engineers & tim CS 24/7", "[Faktor Penentu]\nKeberhasilan sistem bertumpu pada adopsi pengguna, literasi keamanan, & respon kurir."],
    ]
    style_table(table_k, col_w_k, headers_k, data_k)

    set_notes(slide_komponen, "Pada slide ini, teori perkuliahan mengenai Enam Komponen Sistem Informasi kita bedah langsung secara spesifik pada arsitektur ekosistem Shopee. Pertama, Perangkat Keras: server cloud AWS/Tencent, smartphone pengguna, hingga scanner barcode kurir SPX. Kedua, Perangkat Lunak: aplikasi Shopee, microservices Go/Java, TiDB, dan Redis. Ketiga, Data: katalog SKU, order escrow, GPS kurir, dan skor SPayLater. Keempat, Jaringan: 4G/5G, CDN Cloudflare, dan API Gateway. Kelima, Prosedur: SOP Garansi Shopee dan SLA kurir. Serta keenam, Manusia: pembeli, penjual, kurir, dan staf IT. Sesuai catatan dosen: secanggih apa pun Shopee, keberhasilannya ditentukan oleh manusianya.")

    # -------------------------------------------------------------
    # SLIDE 6: TABEL 2 (A) - 6 PRINSIP PERANCANGAN SI (1 - 3)
    # -------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "Tabel Analisis 2 (Bagian 1) · Prinsip Perancangan Sistem Informasi", "Matriks Analisis Prinsip 1, 2, dan 3 pada Shopee")

    headers5 = ["No", "Prinsip Perancangan SI", "Definisi Teori Kuliah", "Implementasi Nyata pada Shopee", "Evaluasi Kritis"]
    data5 = [
        [
            "1",
            "Berorientasi\nPengguna\n(User-Oriented)",
            "Rancang sesuai kebutuhan pengguna.\n(Contoh: wawancara pengguna sebelum membuat menu).",
            "• Fitur COD bagi masyarakat unbanked.\n• Fitur chat langsung dengan pedagang.\n• Garansi Shopee perlindungan pembeli.",
            "[Sangat Adaptif]\nSangat adaptif terhadap budaya belanja lokal masyarakat Indonesia."
        ],
        [
            "2",
            "Sederhana\n(Simplicity)",
            "Mudah dipelajari.\n(Contoh: input nilai 3 langkah, bukan 10).",
            "• Checkout 3 langkah (Beli → Voucher Otomatis → Bayar).\n• Fitur pencarian gambar dengan kamera.",
            "[Mulai Dilanggar]\nAkibat bloatware mini-games & pop-up banner bertumpuk."
        ],
        [
            "3",
            "Terintegrasi\n(Integrated)",
            "Tidak ada data ganda.\n(Contoh: satu sumber data mahasiswa).",
            "• Single Source of Truth (1 akun terhubung ke e-commerce, ShopeePay, & Food).\n• Stok produk terpotong serentak saat order.",
            "[Sangat Unggul]\nMencegah overselling & ketidaksinkronan stok fiktif."
        ]
    ]
    widths5 = [Inches(0.6), Inches(2.2), Inches(2.9), Inches(3.3), Inches(2.733)]
    table_shape5 = slide5.shapes.add_table(4, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    style_table(table_shape5.table, widths5, headers5, data5)

    set_notes(slide5, "Tabel kedua adalah Analisis 6 Prinsip Perancangan Sistem Informasi sesuai materi perkuliahan dosen: Prinsip 1 Berorientasi Pengguna diterapkan Shopee lewat fitur COD dan chat penjual. Prinsip 2 Sederhana diterapkan lewat checkout 3 langkah, namun dikritik karena mulai melanggar akibat bloatware game dan iklan. Prinsip 3 Terintegrasi diterapkan lewat Single Source of Truth di mana 1 akun terhubung ke ShopeePay, SPayLater, dan Food, serta stok terpotong serentak.")

    # -------------------------------------------------------------
    # SLIDE 6: TABEL 2 (B) - 6 PRINSIP PERANCANGAN SI (4 - 6)
    # -------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide6)
    add_header(slide6, "Tabel Analisis 2 (Bagian 2) · Prinsip Perancangan Sistem Informasi", "Matriks Analisis Prinsip 4, 5, dan 6 pada Shopee")

    headers6 = ["No", "Prinsip Perancangan SI", "Definisi Teori Kuliah", "Implementasi Nyata pada Shopee", "Evaluasi Kritis"]
    data6 = [
        [
            "4",
            "Aman\n(Security)",
            "Hak akses sesuai peran.\n(Contoh: mahasiswa, dosen, admin berbeda).",
            "• Role-Based Access: Pembeli, Merchant Seller Centre, Kurir SPX, Admin internal.\n• Enkripsi TLS 1.3, PIN ShopeePay, & 2FA.",
            "[Server Aman]\nInfrastruktur aman, namun rentan penipuan phising/OTP di sisi pengguna."
        ],
        [
            "5",
            "Mudah Dipelihara\n(Maintainable)",
            "Mudah diperbaiki dan diperbarui.\n(Contoh: kode & dokumentasi rapi).",
            "• Arsitektur Microservices independen.\n• Update fitur ShopeeFood tanpa mematikan modul transaksi belanja inti.",
            "[Tinggi]\nPembaruan bug mingguan kontinu via modern CI/CD pipeline."
        ],
        [
            "6",
            "Dapat Dikembangkan\n(Scalable)",
            "Siap bertumbuh.\n(Contoh: tetap lancar dari 1.000 ke 5.000 mahasiswa).",
            "• Cloud Auto-Scaling (AWS & Tencent Cloud).\n• Database terdistribusi (TiDB, Redis Cache, & Message Queue Kafka).",
            "[Sangat Tangguh]\nMenahan lonjakan puluhan juta pesanan serentak promo 11.11."
        ]
    ]
    widths6 = [Inches(0.6), Inches(2.2), Inches(2.9), Inches(3.3), Inches(2.733)]
    table_shape6 = slide6.shapes.add_table(4, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    style_table(table_shape6.table, widths6, headers6, data6)

    set_notes(slide6, "Melanjutkan Tabel Analisis Prinsip 4 sampai 6: Prinsip 4 Aman diterapkan lewat Role-Based Access Control ketat antara pembeli, penjual di Seller Centre, kurir SPX, dan enkripsi TLS 1.3. Prinsip 5 Mudah Dipelihara diterapkan melalui arsitektur Microservices Go dan Java sehingga perbaikan modul tidak mematikan sistem. Prinsip 6 Dapat Dikembangkan diterapkan lewat Cloud Auto-Scaling yang mampu memproses lonjakan pesanan puluhan juta saat festival belanja 11.11.")

    # -------------------------------------------------------------
    # SLIDE 7: BEDAH KASUS DISKUSI DOSEN
    # -------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide7)
    add_header(slide7, "Bedah Kasus Pertanyaan Dosen", "\"Aplikasi Canggih tapi Pengguna Kembali ke Kertas: Prinsip Mana yang Dilanggar?\"")

    box_w = Inches(5.72)
    
    # Left Card: Prinsip Dilanggar
    card_l = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.6), box_w, Inches(5.3))
    card_l.fill.solid()
    card_l.fill.fore_color.rgb = SURFACE_COLOR
    card_l.line.color.rgb = RED
    card_l.line.width = Pt(1.5)

    tx_l = slide7.shapes.add_textbox(Inches(1.1), Inches(1.8), box_w - Inches(0.6), Inches(4.8))
    tf_l = tx_l.text_frame
    tf_l.word_wrap = True
    
    p = tf_l.paragraphs[0]
    p.text = "⚠️ 2 PRINSIP UTAMA YANG DILANGGAR"
    p.font.name = FONT_MAIN
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = RED
    p.space_after = Pt(16)

    p1 = tf_l.add_paragraph()
    p1.text = "1. Prinsip \"Sederhana\" (Simplicity):"
    p1.font.bold = True
    p1.font.size = Pt(13)
    p1.font.color.rgb = TEXT_WHITE

    p1_sub = tf_l.add_paragraph()
    p1_sub.text = "Alur kerja di aplikasi terlalu banyak langkah, berbelit-belit, dan lambat dibandingkan kecepatan mencatat instan di kertas."
    p1_sub.font.size = Pt(11.5)
    p1_sub.font.color.rgb = TEXT_MUTED
    p1_sub.space_after = Pt(16)

    p2 = tf_l.add_paragraph()
    p2.text = "2. Prinsip \"Berorientasi Pengguna\" (User-Oriented):"
    p2.font.bold = True
    p2.font.size = Pt(13)
    p2.font.color.rgb = TEXT_WHITE

    p2_sub = tf_l.add_paragraph()
    p2_sub.text = "Sistem dibangun berdasarkan asumsi canggih pengembang (developer-centric), bukan kemudahan alur kerja nyata pengguna di lapangan (user-centric)."
    p2_sub.font.size = Pt(11.5)
    p2_sub.font.color.rgb = TEXT_MUTED

    # Right Card: Contoh Konkret Shopee
    card_r = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.6), box_w, Inches(5.3))
    card_r.fill.solid()
    card_r.fill.fore_color.rgb = SURFACE_COLOR
    card_r.line.color.rgb = ACCENT_ORANGE
    card_r.line.width = Pt(1.5)

    tx_r = slide7.shapes.add_textbox(Inches(7.1), Inches(1.8), box_w - Inches(0.6), Inches(4.8))
    tf_r = tx_r.text_frame
    tf_r.word_wrap = True

    p = tf_r.paragraphs[0]
    p.text = "💡 CONTOH KONKRET PADA EKOSISTEM SHOPEE"
    p.font.name = FONT_MAIN
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = ACCENT_ORANGE
    p.space_after = Pt(16)

    pr1 = tf_r.add_paragraph()
    pr1.text = "Kasus Nyata Pedagang UMKM Tradisional:"
    pr1.font.bold = True
    pr1.font.size = Pt(13)
    pr1.font.color.rgb = TEXT_WHITE

    pr1_sub = tf_r.add_paragraph()
    pr1_sub.text = "Banyak pedagang pasar offline enggan beralih ke pembukuan digital Shopee karena menu voucher, perhitungan biaya admin, dan skema komisi dirasa terlalu rumit dibandingkan menulis nota manual di kertas."
    pr1_sub.font.size = Pt(11.5)
    pr1_sub.font.color.rgb = TEXT_MUTED
    pr1_sub.space_after = Pt(20)

    pr2 = tf_r.add_paragraph()
    pr2.text = "Pelajaran Kunci Rekayasa SI:"
    pr2.font.bold = True
    pr2.font.size = Pt(13)
    pr2.font.color.rgb = GREEN

    pr2_sub = tf_r.add_paragraph()
    pr2_sub.text = "\"Secanggih apa pun teknologi Cloud/AI, jika melanggar prinsip Sederhana dan User-Oriented, sistem pada akhirnya akan ditinggalkan oleh penggunanya.\""
    pr2_sub.font.size = Pt(12)
    pr2_sub.font.color.rgb = TEXT_WHITE

    set_notes(slide7, "Di materi perkuliahan ada pertanyaan diskusi penting: 'Aplikasi canggih tetapi pengguna kembali ke kertas, prinsip mana yang dilanggar?'. Dalam analisis saya, ada 2 prinsip yang dilanggar: Prinsip Sederhana karena alur sistem terlalu berbelit dan lambat dibanding kertas, serta Prinsip Berorientasi Pengguna karena sistem dibuat berdasarkan keinginan programmer, bukan kebiasaan nyata pengguna. Pada Shopee, ini nyata terjadi pada pedagang UMKM tradisional yang lebih nyaman mencatat bon kertas manual karena menu komisi Shopee dirasa terlalu rumit.")

    # -------------------------------------------------------------
    # SLIDE 8: TABEL 3 - ANALISIS KLASIFIKASI JENIS SI
    # -------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide8)
    add_header(slide8, "Tabel Analisis 3 · Taksonomi Sistem Informasi", "Matriks Klasifikasi 4 Jenis Sistem Informasi pada Shopee")

    headers8 = ["Jenis Sistem Informasi", "Level / Pengguna", "Alasan Pengelompokan (Kaidah SI)", "Fitur & Implementasi Nyata", "Dampak Bisnis"]
    data8 = [
        [
            "1. TPS\n(Transaction\nProcessing System)",
            "Level Operasional\n(Pembeli & Kasir)",
            "Memproses jutaan transaksi bersamaan dengan kepatuhan penuh kaidah ACID agar saldo dan stok akurat.",
            "• Checkout & potong saldo ShopeePay\n• Kunci kuota stok flash sale",
            "Kepastian transaksi harian tanpa selisih uang atau overselling."
        ],
        [
            "2. MIS\n(Management\nInformation System)",
            "Level Manajerial\n(Pemilik Toko/Merchant)",
            "Mengubah data transaksi mentah TPS menjadi laporan analitik terstruktur dan grafik performa toko.",
            "• Shopee Seller Centre Dashboard\n• Grafik omzet & tren kata kunci",
            "Membantu merchant merencanakan persediaan stok barang secara tepat."
        ],
        [
            "3. DSS\n(Decision Support\nSystem)",
            "Level Analitik Cerdas\n(Sistem AI & Analis)",
            "Menerapkan algoritma analitik prediktif dan Machine Learning untuk keputusan semi-terstruktur otomatis.",
            "• AI Credit Scoring SPayLater\n• Dynamic discount & rute kurir SPX",
            "Menekan rasio kredit macet (NPL) dan menghemat biaya rute kurir."
        ],
        [
            "4. IOS\n(Inter-Organizational\nSystem)",
            "Lintas Organisasi\n(Shopee ↔ Bank ↔ Ekspedisi)",
            "Mengintegrasikan aliran data proses bisnis antar-perusahaan otomatis via B2B Open API.",
            "• Open API Virtual Account Bank\n• Integrasi resi eksternal (J&T, SiCepat)",
            "Status pembayaran otomatis lunas seketika tanpa jeda manual."
        ]
    ]
    widths8 = [Inches(2.1), Inches(1.9), Inches(2.8), Inches(2.6), Inches(2.333)]
    table_shape8 = slide8.shapes.add_table(5, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    style_table(table_shape8.table, widths8, headers8, data8)

    set_notes(slide8, "Tabel ketiga adalah Tabel Analisis Klasifikasi Jenis Sistem Informasi di Shopee: TPS di level operasional memproses jutaan checkout real-time dengan kaidah ACID. MIS di level manajerial lewat Shopee Seller Centre mengubah data mentah transaksi menjadi grafik laporan omzet toko. DSS di level analitik cerdas menerapkan AI untuk penentuan limit kredit SPayLater dan rute kurir. Dan IOS menghubungkan Shopee ke sistem perbankan dan ekspedisi secara terpadu tanpa campur tangan manual.")

    # -------------------------------------------------------------
    # SLIDE 9: TABEL 4 - ANALISIS EVALUASI PERANCANGAN SISTEM
    # -------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide9)
    add_header(slide9, "Tabel Analisis 4 · Evaluasi Perancangan Sistem Informasi", "Matriks Evaluasi: Kelebihan, Kelemahan, & Rekomendasi Solusi")

    headers9 = ["Dimensi Evaluasi", "Temuan & Fakta Lapangan", "Prinsip SI Terkait", "Dampak / Risiko", "Rekomendasi Solusi"]
    data9 = [
        [
            "1. Kelebihan\n(Strengths)",
            "• Skalabilitas microservices cloud tinggi.\n• Integrasi ekosistem lock-in (belanja, paylater, kurir).\n• Personalisasi belanja AI.",
            "• Dapat Dikembangkan\n• Terintegrasi\n• User-Oriented",
            "Retensi pengguna sangat kuat & konversi penjualan tinggi.",
            "Pertahankan modularitas layanan mandiri dan perkuat ekosistem perbankan digital."
        ],
        [
            "2. Kelemahan\n(Weaknesses)",
            "• Application Bloatware: Kelebihan fitur non-core (games, video pendek, live stream).\n• Flash Sale Latency: Request timeout pada detik pertama promo 1 rupiah.",
            "• Melanggar Prinsip Sederhana\n• Tantangan Prinsip Scalability",
            "Aplikasi boros memori RAM, lambat, dan baterai cepat panas di HP entry-level.",
            "Terapkan Micro-Frontends atau rilis resmi Shopee Lite (khusus core e-commerce)."
        ],
        [
            "3. Keamanan\n(Security)",
            "• Social Engineering: Pengguna awam rentan tertipu telepon/pesan oknum yang meminta kode SMS OTP.",
            "• Celah Prinsip Aman\n(Human Factor)",
            "Pembobolan akun dan penyalahgunaan limit kredit SPayLater.",
            "Gantikan SMS OTP dengan otentikasi biometrik FIDO2 Passkeys (Sidik Jari / Face ID)."
        ]
    ]
    widths9 = [Inches(1.8), Inches(3.0), Inches(2.1), Inches(2.3), Inches(2.533)]
    table_shape9 = slide9.shapes.add_table(4, 5, Inches(0.8), Inches(1.6), Inches(11.733), Inches(5.3))
    style_table(table_shape9.table, widths9, headers9, data9)

    set_notes(slide9, "Tabel keempat adalah Tabel Analisis Evaluasi Perancangan Sistem: Kelebihannya adalah skalabilitas microservices yang sangat tinggi saat 11.11 dan integrasi ekosistem yang rapat. Kelemahannya adalah terjadinya Application Bloatware yang membuat aplikasi berat dan nge-lag di HP spek rendah, serta latency saat flash sale. Celah keamanannya ada pada rekayasa sosial penipuan OTP. Saya merekomendasikan solusi Shopee Lite dan biometrik FIDO2 Passkeys.")

    # -------------------------------------------------------------
    # SLIDE 10: VALIDASI FAKTUAL
    # -------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide10)
    add_header(slide10, "Landasan Data & Validasi Akademik", "Validasi Faktual: 4 Sumber Resmi Analisis Sistem Shopee")

    sources = [
        ("1. Shopee Engineering Blog", "Dokumentasi resmi arsitektur backend microservices Go/Java, caching in-memory Redis, dan distributed SQL TiDB.", ACCENT_ORANGE),
        ("2. Laporan Sea Limited (NYSE: SE)", "Laporan keterbukaan bursa saham yang memvalidasi infrastruktur cloud Tencent & AWS serta volume transaksi jutaan order per hari.", BLUE),
        ("3. Regulasi OJK & Bank Indonesia", "Bukti legalitas SPayLater (PT Commerce Finance) dengan sistem scoring AI terhubung ke SLIK OJK dan Virtual Account bank.", PURPLE),
        ("4. Ketentuan Resmi Garansi Shopee", "Mekanisme Rekening Penampung (Escrow Account) dan SLA kurir SPX Express yang membuktikan keandalan proses transaksi.", GREEN),
    ]

    grid_w = Inches(5.72)
    grid_h = Inches(2.4)
    positions = [
        (Inches(0.8), Inches(1.7)),
        (Inches(6.8), Inches(1.7)),
        (Inches(0.8), Inches(4.45)),
        (Inches(6.8), Inches(4.45))
    ]

    for i, (title, desc, color) in enumerate(sources):
        gx, gy = positions[i]
        card = slide10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, gx, gy, grid_w, grid_h)
        card.fill.solid()
        card.fill.fore_color.rgb = SURFACE_COLOR
        card.line.color.rgb = BORDER_COLOR
        card.line.width = Pt(1)

        # Indicator badge line on left
        ind = slide10.shapes.add_shape(MSO_SHAPE.RECTANGLE, gx, gy, Inches(0.12), grid_h)
        ind.fill.solid()
        ind.fill.fore_color.rgb = color
        ind.line.fill.background()

        tx = slide10.shapes.add_textbox(gx + Inches(0.35), gy + Inches(0.25), grid_w - Inches(0.6), grid_h - Inches(0.5))
        tf = tx.text_frame
        tf.word_wrap = True

        p1 = tf.paragraphs[0]
        p1.text = title
        p1.font.name = FONT_MAIN
        p1.font.bold = True
        p1.font.size = Pt(13)
        p1.font.color.rgb = color
        p1.space_after = Pt(8)

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.name = FONT_MAIN
        p2.font.size = Pt(11)
        p2.font.color.rgb = TEXT_MUTED

    set_notes(slide10, "Sebelum menutup, saya tegaskan bahwa seluruh data pada tabel analisis ini berlandaskan fakta resmi: Shopee Engineering Blog untuk arsitektur microservices Go/Java dan database Redis, Laporan Keterbukaan Sea Limited di bursa saham NYSE untuk data cloud Tencent dan AWS, Regulasi OJK untuk operasional SPayLater, serta ketentuan resmi Garansi Shopee.")

    # -------------------------------------------------------------
    # SLIDE 11: VIDEO PRESENTASI
    # -------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide11)
    add_header(slide11, "Media Pendukung", "Video Presentasi & Demonstrasi Sistem")

    # Center box representing video
    v_box = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(2.2), Inches(1.7), Inches(8.933), Inches(5.1))
    v_box.fill.solid()
    v_box.fill.fore_color.rgb = SURFACE_COLOR
    v_box.line.color.rgb = BORDER_COLOR
    v_box.line.width = Pt(1.5)

    # Play badge or indicator
    play_icon = slide11.shapes.add_shape(MSO_SHAPE.ISOSCELES_TRIANGLE, Inches(6.3), Inches(3.4), Inches(0.8), Inches(0.8))
    play_icon.rotation = 90
    play_icon.fill.solid()
    play_icon.fill.fore_color.rgb = ACCENT_ORANGE
    play_icon.line.fill.background()

    v_tx = slide11.shapes.add_textbox(Inches(2.5), Inches(4.5), Inches(8.333), Inches(1.8))
    tf_v = v_tx.text_frame
    tf_v.word_wrap = True
    
    pv1 = tf_v.paragraphs[0]
    pv1.text = "Video Pendukung: video.mp4"
    pv1.alignment = PP_ALIGN.CENTER
    pv1.font.name = FONT_MAIN
    pv1.font.bold = True
    pv1.font.size = Pt(16)
    pv1.font.color.rgb = TEXT_WHITE
    pv1.space_after = Pt(6)

    pv2 = tf_v.add_paragraph()
    pv2.text = "Tersedia file terpisah video.mp4 di folder proyek untuk pemutaran video demonstrasi interaktif."
    pv2.alignment = PP_ALIGN.CENTER
    pv2.font.name = FONT_MAIN
    pv2.font.size = Pt(12)
    pv2.font.color.rgb = TEXT_MUTED

    set_notes(slide11, "Video pendukung presentasi mengenai demonstrasi aplikasi dan alur interaksi pengguna Shopee.")

    # -------------------------------------------------------------
    # SLIDE 12: PENUTUP & Q&A
    # -------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide12)

    # Decorative Card
    card_end = slide12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(5.9))
    card_end.fill.solid()
    card_end.fill.fore_color.rgb = RGBColor(16, 22, 36)
    card_end.line.color.rgb = RGBColor(38, 50, 77)
    card_end.line.width = Pt(1.5)

    # Orange top accent line
    top_bar_end = slide12.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(0.8), Inches(11.733), Inches(0.08))
    top_bar_end.fill.solid()
    top_bar_end.fill.fore_color.rgb = ACCENT_ORANGE
    top_bar_end.line.fill.background()

    txBox = slide12.shapes.add_textbox(Inches(1.5), Inches(1.5), Inches(10.333), Inches(4.5))
    tf = txBox.text_frame
    tf.word_wrap = True

    p_k = tf.paragraphs[0]
    p_k.text = "SESI DISKUSI AKADEMIK"
    p_k.font.name = FONT_MAIN
    p_k.font.size = Pt(13)
    p_k.font.bold = True
    p_k.font.color.rgb = ACCENT_ORANGE
    p_k.space_after = Pt(18)

    p_t = tf.add_paragraph()
    p_t.text = "Terima Kasih atas Perhatian Anda."
    p_t.font.name = FONT_MAIN
    p_t.font.size = Pt(36)
    p_t.font.bold = True
    p_t.font.color.rgb = TEXT_WHITE
    p_t.space_after = Pt(18)

    p_q = tf.add_paragraph()
    p_q.text = "\"Sistem Informasi yang unggul bukan sekadar yang paling canggih, melainkan yang paling sederhana, andal, dan menjawab kebutuhan nyata penggunanya.\""
    p_q.font.name = FONT_MAIN
    p_q.font.size = Pt(15)
    p_q.font.italic = True
    p_q.font.color.rgb = TEXT_MUTED
    p_q.space_after = Pt(36)

    # QA Badge
    badge = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(4.7), Inches(5.8), Inches(0.7))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(45, 25, 25)
    badge.line.color.rgb = ACCENT_ORANGE
    badge.line.width = Pt(1.5)

    tf_badge = badge.text_frame
    tf_badge.text = "Silakan, Sesi Tanya Jawab (Q&A) Saya Buka 💬"
    tf_badge.paragraphs[0].alignment = PP_ALIGN.CENTER
    tf_badge.paragraphs[0].font.name = FONT_MAIN
    tf_badge.paragraphs[0].font.bold = True
    tf_badge.paragraphs[0].font.size = Pt(13)
    tf_badge.paragraphs[0].font.color.rgb = ACCENT_ORANGE

    set_notes(slide12, "Sebagai kesimpulan akhir: Penyajian dalam bentuk tabel analisis ini memperlihatkan bahwa arsitektur Sistem Informasi Shopee telah memenuhi prinsip integrasi, keamanan akses, dan skalabilitas tinggi. Namun penegakan prinsip kesederhanaan dan perlindungan dari rekayasa sosial tetap menjadi catatan kritis ke depan. Terima kasih banyak atas perhatian Bapak/Ibu dosen dan rekan-rekan, sesi tanya jawab saya buka!")

    # Save to all target locations
    output_path1 = os.path.join(os.getcwd(), "Presentasi_Analisis_SI_Shopee.pptx")
    output_path2 = os.path.join(os.getcwd(), "bolt-slides-main", "Presentasi_Analisis_SI_Shopee.pptx")
    output_path3 = os.path.join(os.getcwd(), "Presentasi_Analisis_SI_Shopee_MUH IKRAM.pptx")
    prs.save(output_path1)
    prs.save(output_path2)
    prs.save(output_path3)
    print(f"Presentation saved successfully to:\n1. {output_path1}\n2. {output_path2}\n3. {output_path3}")

if __name__ == "__main__":
    create_deck()
