import Deck from './deck/Deck';
import Slide from './deck/Slide';
import Build from './deck/Build';
import Reveal from './deck/Reveal';
import Cover from './components/Cover';
import Agenda from './components/Agenda';

const BASE = import.meta.env.BASE_URL;

const card: React.CSSProperties = {
  padding: '20px',
  borderRadius: 'var(--radius)',
  background: 'var(--surface)',
  border: '1px solid var(--hair)',
};

const tableContainer: React.CSSProperties = {
  width: '100%',
  overflowX: 'auto',
  borderRadius: 'var(--radius-sm)',
  border: '1px solid var(--hair)',
  background: 'var(--surface)',
  marginTop: '12px',
};

const tableStyle: React.CSSProperties = {
  width: '100%',
  borderCollapse: 'collapse',
  fontSize: '0.80rem',
  lineHeight: 1.5,
  textAlign: 'left',
};

const thStyle: React.CSSProperties = {
  background: 'var(--surface-2)',
  color: 'var(--primary)',
  fontWeight: 700,
  fontSize: '0.74rem',
  textTransform: 'uppercase',
  letterSpacing: '0.06em',
  padding: '10px 12px',
  borderBottom: '1px solid var(--hair)',
  whiteSpace: 'nowrap',
};

const tdStyle: React.CSSProperties = {
  padding: '9px 12px',
  borderBottom: '1px solid var(--hair-2)',
  color: 'var(--fg-muted)',
  verticalAlign: 'top',
};

const tdBold: React.CSSProperties = {
  ...tdStyle,
  color: 'var(--fg)',
  fontWeight: 600,
  whiteSpace: 'nowrap',
};

export default function App() {
  return (
    <Deck>
      {/* ─────────────────────────────────────────────────────────────
          SLIDE 1: COVER
          ───────────────────────────────────────────────────────────── */}
      <Cover
        nav="Cover"
        notes="Selamat pagi/siang Bapak/Ibu dosen penguji serta rekan-rekan sekalian. Pada presentasi 15 menit hari ini, saya akan menyajikan tugas analisis Sistem Informasi Shopee yang disusun secara terstruktur dalam bentuk Tabel Analisis Akademik, mencakup Model IPO, 6 Prinsip Perancangan SI, Klasifikasi Sistem, hingga Evaluasi Arsitekturnya."
        kicker="Tugas Sistem Informasi · Format Tabel Analisis"
        title={
          <>
            Tabel Analisis SI <span className="accent-text">Shopee</span>
          </>
        }
        subtitle="Penyajian Terstruktur: Tabel Analisis IPO 4 Pilar, Tabel 6 Prinsip Perancangan SI, Taksonomi Jenis SI, & Evaluasi Arsitektur."
        foot="Presentasi Individu 15 Menit · Program Studi Sistem Informasi"
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 2: AGENDA PRESENTASI
          ───────────────────────────────────────────────────────────── */}
      <Agenda
        nav="Agenda"
        notes="Seluruh materi tugas ini telah saya sesuaikan ke dalam format matriks tabel analisis: Dimulai dari Tabel Analisis IPO lintas 4 pilar ekosistem, dilanjutkan Tabel Analisis 6 Prinsip Perancangan SI sesuai materi kuliah, Tabel Klasifikasi Taksonomi SI, dan ditutup dengan Tabel Evaluasi Kritis Kelebihan, Kelemahan, serta Rekomendasi Solusinya."
        kicker="Struktur Tugas (Format Tabel Analisis)"
        title="Daftar Tabel Analisis Pembahasan"
        items={[
          { title: 'Tabel 1: Analisis Model Input – Proses – Output (IPO)', hint: '4 Pilar Ekosistem Shopee' },
          { title: 'Tabel 2: Analisis 6 Prinsip Perancangan Sistem Informasi', hint: 'Sesuai Slide Teori Perkuliahan' },
          { title: 'Tabel 3: Analisis Klasifikasi Jenis Sistem Informasi', hint: 'TPS, MIS, DSS, & IOS Beserta Alasannya' },
          { title: 'Tabel 4: Analisis Evaluasi Perancangan Sistem', hint: 'Kelebihan, Bloatware, & Solusi Rekayasa SI' },
          { title: 'Validasi Faktual & Sesi Diskusi Tanya Jawab (Q&A)', hint: 'Rujukan Resmi & Diskusi' },
        ]}
      />

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 3: TABEL 1 - ANALISIS MODEL IPO (4 PILAR)
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Tabel 1: Analisis IPO"
        notes="Tabel pertama adalah Tabel Analisis IPO pada 4 pilar ekosistem Shopee: Pilar Pembeli menerima input keranjang dan bayar, diproses lewat Garansi Shopee dan verifikasi OTP, menghasilkan invoice dan live tracking kurir. Pilar Penjual menerima katalog produk, diproses kalkulasi komisi dan SEO, menghasilkan label resi dan saldo toko. Pilar FinTech SPayLater memproses KTP dan credit scoring, menghasilkan limit kredit. Pilar Logistik SPX memproses scan resi dan optimasi rute kurir, menghasilkan bukti serah terima paket."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Tabel Analisis 1 · Siklus Input – Proses – Output (IPO)
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '10px',
            }}
          >
            Matriks Analisis IPO pada 4 Pilar Ekosistem Shopee
          </h2>
        </Reveal>

        <div style={tableContainer}>
          <table style={tableStyle}>
            <thead>
              <tr>
                <th style={thStyle}>Pilar / Entitas Sistem</th>
                <th style={thStyle}>📥 Input (Masukan)</th>
                <th style={thStyle}>⚙️ Proses (Logika Bisnis)</th>
                <th style={thStyle}>📤 Output (Keluaran)</th>
                <th style={thStyle}>Fitur Terkait</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={tdBold}>1. Sisi Pembeli (Buyer)</td>
                <td style={tdStyle}>• Barang keranjang (cart)<br />• Alamat & titik GPS<br />• Opsi bayar & voucher</td>
                <td style={tdStyle}>• Validasi 2FA / OTP<br />• Garansi Shopee (Escrow)<br />• Kunci kuota stok real-time</td>
                <td style={tdStyle}>• Resi otomatis & e-invoice<br />• Peta live tracking kurir<br />• Notifikasi status paket</td>
                <td style={tdStyle}><span style={{ color: 'var(--primary)', fontWeight: 600 }}>Checkout & SPX Tracking</span></td>
              </tr>
              <tr>
                <td style={tdBold}>2. Sisi Penjual (Merchant)</td>
                <td style={tdStyle}>• Master SKU & stok riil<br />• Foto produk & harga<br />• Balasan chat pembeli</td>
                <td style={tdStyle}>• Index algoritma pencarian<br />• Potongan komisi Shopee<br />• Poin penalti keterlambatan</td>
                <td style={tdStyle}>• PDF Shipping Label resi<br />• Pencairan Saldo Penjual<br />• Laporan omzet & performa</td>
                <td style={tdStyle}><span style={{ color: 'var(--primary)', fontWeight: 600 }}>Shopee Seller Centre</span></td>
              </tr>
              <tr>
                <td style={tdBold}>3. Sisi FinTech (SPayLater)</td>
                <td style={tdStyle}>• Foto e-KTP & selfie wajah<br />• Kontak darurat & gaji<br />• Pengajuan limit kredit</td>
                <td style={tdStyle}>• AI Credit Scoring engine<br />• Pengecekan histori SLIK OJK<br />• Deteksi anti-fraud & bunga</td>
                <td style={tdStyle}>• Saldo limit cicilan aktif<br />• Persetujuan transaksi<br />• Billing statement bulanan</td>
                <td style={tdStyle}><span style={{ color: '#0284c7', fontWeight: 600 }}>SPayLater & ShopeePay</span></td>
              </tr>
              <tr>
                <td style={tdBold}>4. Sisi Logistik (SPX)</td>
                <td style={tdStyle}>• Scan barcode resi di hub<br />• GPS kurir pengantar<br />• Foto penerimaan paket</td>
                <td style={tdStyle}>• Algoritma optimasi rute<br />• Klasterisasi wilayah antar<br />• Estimasi waktu tiba (ETA)</td>
                <td style={tdStyle}>• Foto bukti kirim (POD)<br />• Status paket "Terkirim"<br />• Update riwayat lacak resi</td>
                <td style={tdStyle}><span style={{ color: '#059669', fontWeight: 600 }}>Shopee Xpress Driver</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 4: BUKTI VISUAL LAYAR SHOPEE
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Bukti Visual IPO"
        notes="Untuk melengkapi tabel analisis IPO tadi, di slide ini saya lampirkan bukti visual nyata dari aplikasi Shopee: Gambar pertama membuktikan Input di halaman Checkout saat memilih barang dan alamat. Gambar kedua membuktikan Proses sistem Garansi Shopee di mana pembayaran ditahan di rekening penampung. Gambar ketiga membuktikan Output peta pelacakan posisi kurir SPX secara live."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Lampiran Visual · Pembuktian Alur IPO
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '14px',
            }}
          >
            Tangkapan Layar Nyata Alur IPO Belanja di Shopee
          </h2>
        </Reveal>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
            gap: 16,
            alignItems: 'stretch',
          }}
        >
          {/* Card 1: Input */}
          <div style={card}>
            <div style={{ position: 'relative', borderRadius: '10px', overflow: 'hidden', marginBottom: 10, border: '1px solid var(--hair)' }}>
              <img src={`${BASE}images/shopee_input.jpg`} alt="Checkout Input" style={{ width: '100%', height: '140px', objectFit: 'cover', display: 'block' }} />
              <span style={{ position: 'absolute', top: 6, left: 6, background: '#ee4d2d', color: '#fff', fontSize: 10, fontWeight: 700, padding: '2px 7px', borderRadius: 4 }}>
                1. INPUT
              </span>
            </div>
            <div style={{ fontWeight: 700, fontSize: 14, color: 'var(--fg)', marginBottom: 4 }}>Halaman Checkout & Cart</div>
            <div style={{ fontSize: 12, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Input data barang di keranjang, kupon voucher, dan titik koordinat GPS alamat pengiriman.
            </div>
          </div>

          {/* Card 2: Process */}
          <div style={card}>
            <div style={{ position: 'relative', borderRadius: '10px', overflow: 'hidden', marginBottom: 10, border: '1px solid var(--hair)' }}>
              <img src={`${BASE}images/shopee_process.jpg`} alt="Garansi Shopee Process" style={{ width: '100%', height: '140px', objectFit: 'cover', display: 'block' }} />
              <span style={{ position: 'absolute', top: 6, left: 6, background: '#0284c7', color: '#fff', fontSize: 10, fontWeight: 700, padding: '2px 7px', borderRadius: 4 }}>
                2. PROSES
              </span>
            </div>
            <div style={{ fontWeight: 700, fontSize: 14, color: 'var(--fg)', marginBottom: 4 }}>Garansi Shopee (Escrow Lock)</div>
            <div style={{ fontSize: 12, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Pemrosesan rekening bersama penahan dana aman, verifikasi PIN/OTP, dan penguncian stok toko.
            </div>
          </div>

          {/* Card 3: Output */}
          <div style={card}>
            <div style={{ position: 'relative', borderRadius: '10px', overflow: 'hidden', marginBottom: 10, border: '1px solid var(--hair)' }}>
              <img src={`${BASE}images/shopee_output.jpg`} alt="Tracking Output" style={{ width: '100%', height: '140px', objectFit: 'cover', display: 'block' }} />
              <span style={{ position: 'absolute', top: 6, left: 6, background: '#059669', color: '#fff', fontSize: 10, fontWeight: 700, padding: '2px 7px', borderRadius: 4 }}>
                3. OUTPUT
              </span>
            </div>
            <div style={{ fontWeight: 700, fontSize: 14, color: 'var(--fg)', marginBottom: 4 }}>Live Tracking Peta & Resi</div>
            <div style={{ fontSize: 12, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Keluaran nomor resi pengiriman otomatis, dokumen e-invoice, dan pergerakan kurir di peta GPS.
            </div>
          </div>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 5: TABEL 2 (A) - 6 PRINSIP PERANCANGAN SI (PRINSIP 1 - 3)
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Tabel 2: Prinsip 1-3"
        notes="Tabel kedua adalah Analisis 6 Prinsip Perancangan Sistem Informasi sesuai materi perkuliahan dosen: Prinsip 1 Berorientasi Pengguna diterapkan Shopee lewat fitur COD dan chat penjual. Prinsip 2 Sederhana diterapkan lewat checkout 3 langkah, namun dikritik karena mulai melanggar akibat bloatware game dan iklan. Prinsip 3 Terintegrasi diterapkan lewat Single Source of Truth di mana 1 akun terhubung ke ShopeePay, SPayLater, dan Food, serta stok terpotong serentak."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Tabel Analisis 2 (Bagian 1) · Prinsip Perancangan Sistem Informasi
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '10px',
            }}
          >
            Matriks Analisis Prinsip 1, 2, dan 3 pada Shopee
          </h2>
        </Reveal>

        <div style={tableContainer}>
          <table style={tableStyle}>
            <thead>
              <tr>
                <th style={thStyle}>No</th>
                <th style={thStyle}>Prinsip Perancangan SI</th>
                <th style={thStyle}>Definisi Teori Kuliah</th>
                <th style={thStyle}>Implementasi Nyata pada Shopee</th>
                <th style={thStyle}>Evaluasi Kritis</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={tdBold}>1</td>
                <td style={tdBold}>Berorientasi Pengguna</td>
                <td style={tdStyle}>Rancang sesuai kebutuhan pengguna. (Contoh: wawancara pengguna sebelum membuat menu).</td>
                <td style={tdStyle}>• Fitur COD bagi masyarakat unbanked.<br />• Fitur chat langsung dengan pedagang.<br />• Garansi Shopee perlindungan pembeli.</td>
                <td style={tdStyle}><span style={{ color: '#10b981', fontWeight: 600 }}>Sangat adaptif</span> terhadap budaya belanja lokal Indonesia.</td>
              </tr>
              <tr>
                <td style={tdBold}>2</td>
                <td style={tdBold}>Sederhana</td>
                <td style={tdStyle}>Mudah dipelajari. (Contoh: input nilai 3 langkah, bukan 10).</td>
                <td style={tdStyle}>• Checkout 3 langkah (Beli → Voucher Otomatis → Bayar).<br />• Fitur pencarian gambar dengan kamera.</td>
                <td style={tdStyle}><span style={{ color: '#ef4444', fontWeight: 600 }}>Mulai dilanggar</span> akibat bloatware mini-games & pop-up bertumpuk.</td>
              </tr>
              <tr>
                <td style={tdBold}>3</td>
                <td style={tdBold}>Terintegrasi</td>
                <td style={tdStyle}>Tidak ada data ganda. (Contoh: satu sumber data mahasiswa).</td>
                <td style={tdStyle}>• Single Source of Truth (1 akun terhubung ke e-commerce, ShopeePay, & Food).<br />• Stok produk terpotong serentak saat order.</td>
                <td style={tdStyle}><span style={{ color: '#10b981', fontWeight: 600 }}>Sangat unggul</span>, mencegah overselling stok fiktif.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 6: TABEL 2 (B) - 6 PRINSIP PERANCANGAN SI (PRINSIP 4 - 6)
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Tabel 2: Prinsip 4-6"
        notes="Melanjutkan Tabel Analisis Prinsip 4 sampai 6: Prinsip 4 Aman diterapkan lewat Role-Based Access Control ketat antara pembeli, penjual di Seller Centre, kurir SPX, dan enkripsi TLS 1.3. Prinsip 5 Mudah Dipelihara diterapkan melalui arsitektur Microservices Go dan Java sehingga perbaikan modul tidak mematikan sistem. Prinsip 6 Dapat Dikembangkan diterapkan lewat Cloud Auto-Scaling yang mampu memproses lonjakan pesanan puluhan juta saat festival belanja 11.11."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Tabel Analisis 2 (Bagian 2) · Prinsip Perancangan Sistem Informasi
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '10px',
            }}
          >
            Matriks Analisis Prinsip 4, 5, dan 6 pada Shopee
          </h2>
        </Reveal>

        <div style={tableContainer}>
          <table style={tableStyle}>
            <thead>
              <tr>
                <th style={thStyle}>No</th>
                <th style={thStyle}>Prinsip Perancangan SI</th>
                <th style={thStyle}>Definisi Teori Kuliah</th>
                <th style={thStyle}>Implementasi Nyata pada Shopee</th>
                <th style={thStyle}>Evaluasi Kritis</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={tdBold}>4</td>
                <td style={tdBold}>Aman</td>
                <td style={tdStyle}>Hak akses sesuai peran. (Contoh: mahasiswa, dosen, admin berbeda).</td>
                <td style={tdStyle}>• Role-Based Access: Pembeli, Merchant Seller Centre, Kurir SPX, Admin internal.<br />• Enkripsi TLS 1.3, PIN ShopeePay, & 2FA.</td>
                <td style={tdStyle}><span style={{ color: '#f59e0b', fontWeight: 600 }}>Server aman</span>, namun rentan penipuan phising OTP di sisi pengguna.</td>
              </tr>
              <tr>
                <td style={tdBold}>5</td>
                <td style={tdBold}>Mudah Dipelihara</td>
                <td style={tdStyle}>Mudah diperbaiki dan diperbarui. (Contoh: kode & dokumentasi rapi).</td>
                <td style={tdStyle}>• Arsitektur Microservices independen.<br />• Update fitur ShopeeFood tanpa mematikan modul transaksi belanja inti.</td>
                <td style={tdStyle}><span style={{ color: '#10b981', fontWeight: 600 }}>Tinggi</span>, pembaruan bug mingguan kontinu via CI/CD pipeline.</td>
              </tr>
              <tr>
                <td style={tdBold}>6</td>
                <td style={tdBold}>Dapat Dikembangkan</td>
                <td style={tdStyle}>Siap bertumbuh. (Contoh: tetap lancar dari 1.000 ke 5.000 mahasiswa).</td>
                <td style={tdStyle}>• Cloud Auto-Scaling (AWS & Tencent Cloud).<br />• Database terdistribusi (TiDB, Redis Cache, & Message Queue Kafka).</td>
                <td style={tdStyle}><span style={{ color: '#10b981', fontWeight: 600 }}>Sangat tangguh</span> menahan lonjakan jutaan order saat promo 11.11.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 7: BEDAH KASUS DISKUSI DOSEN
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Studi Kasus Diskusi"
        notes="Di materi perkuliahan ada pertanyaan diskusi penting: 'Aplikasi canggih tetapi pengguna kembali ke kertas, prinsip mana yang dilanggar?'. Dalam analisis saya, ada 2 prinsip yang dilanggar: Prinsip Sederhana karena alur sistem terlalu berbelit dan lambat dibanding kertas, serta Prinsip Berorientasi Pengguna karena sistem dibuat berdasarkan keinginan programmer, bukan kebiasaan nyata pengguna. Pada Shopee, ini nyata terjadi pada pedagang UMKM tradisional yang lebih nyaman mencatat bon kertas manual karena menu komisi Shopee dirasa terlalu rumit."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Bedah Kasus Pertanyaan Dosen
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(20px, 2.8vw, 34px)',
              marginBottom: '14px',
            }}
          >
            "Aplikasi Canggih tapi Pengguna Kembali ke Kertas: Prinsip Mana yang Dilanggar?"
          </h2>
        </Reveal>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(320px, 1fr))',
            gap: 18,
            alignItems: 'stretch',
          }}
        >
          <div style={card}>
            <div style={{ color: '#ef4444', fontWeight: 800, fontSize: 13, textTransform: 'uppercase', marginBottom: 8 }}>
              ⚠️ 2 Prinsip Utama yang Dilanggar
            </div>
            <ul style={{ fontSize: 13, color: 'var(--fg)', lineHeight: 1.6, paddingLeft: 18 }}>
              <li>
                <b>1. Prinsip "Sederhana" (Simplicity):</b><br />
                <span style={{ color: 'var(--fg-muted)' }}>Alur kerja di aplikasi terlalu banyak langkah, berbelit, dan lambat dibandingkan kecepatan mencatat di kertas.</span>
              </li>
              <li style={{ marginTop: 8 }}>
                <b>2. Prinsip "Berorientasi Pengguna" (User-Oriented):</b><br />
                <span style={{ color: 'var(--fg-muted)' }}>Sistem dibangun berdasarkan asumsi canggih pengembang (*developer-centric*), bukan kemudahan alur kerja nyata pengguna di lapangan (*user-centric*).</span>
              </li>
            </ul>
          </div>

          <div style={card}>
            <div style={{ color: 'var(--primary)', fontWeight: 800, fontSize: 13, textTransform: 'uppercase', marginBottom: 8 }}>
              💡 Contoh Konkret pada Ekosistem Shopee
            </div>
            <div style={{ fontSize: 12.5, color: 'var(--fg-muted)', lineHeight: 1.6 }}>
              <p>
                <b>Kasus Nyata Pedagang UMKM Tradisional:</b> Banyak pedagang pasar offline enggan beralih ke pembukuan digital Shopee karena menu voucher, perhitungan biaya admin, dan komisi dirasa terlalu rumit dibandingkan menulis nota manual di kertas.
              </p>
              <p style={{ marginTop: 6, color: 'var(--fg)', fontWeight: 600 }}>
                <b>Pelajaran SI:</b> Secanggih apa pun teknologi Cloud/AI, jika melanggar prinsip <i>Sederhana</i> dan <i>User-Oriented</i>, sistem akan ditinggalkan penggunanya.
              </p>
            </div>
          </div>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 8: TABEL 3 - ANALISIS KLASIFIKASI JENIS SI
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Tabel 3: Klasifikasi SI"
        notes="Tabel ketiga adalah Tabel Analisis Klasifikasi Jenis Sistem Informasi di Shopee: TPS di level operasional memproses jutaan checkout real-time dengan kaidah ACID. MIS di level manajerial lewat Shopee Seller Centre mengubah data mentah transaksi menjadi grafik laporan omzet toko. DSS di level analitik cerdas menerapkan AI untuk penentuan limit kredit SPayLater dan rute kurir. Dan IOS menghubungkan Shopee ke sistem perbankan dan ekspedisi secara terpadu tanpa campur tangan manual."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Tabel Analisis 3 · Taksonomi Sistem Informasi
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '10px',
            }}
          >
            Matriks Klasifikasi 4 Jenis Sistem Informasi pada Shopee
          </h2>
        </Reveal>

        <div style={tableContainer}>
          <table style={tableStyle}>
            <thead>
              <tr>
                <th style={thStyle}>Jenis Sistem Informasi</th>
                <th style={thStyle}>Level / Pengguna</th>
                <th style={thStyle}>Alasan Pengelompokan (Kaidah SI)</th>
                <th style={thStyle}>Fitur & Implementasi Nyata</th>
                <th style={thStyle}>Dampak Bisnis</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={tdBold}>1. TPS (Transaction Processing System)</td>
                <td style={tdStyle}>Level Operasional<br /><i>(Pembeli & Kasir)</i></td>
                <td style={tdStyle}>Memproses jutaan transaksi bersamaan dengan kepatuhan penuh kaidah <b>ACID</b> agar saldo dan stok akurat.</td>
                <td style={tdStyle}>• Checkout & potong saldo ShopeePay<br />• Kunci kuota stok flash sale</td>
                <td style={tdStyle}>Kepastian transaksi harian tanpa selisih uang atau overselling.</td>
              </tr>
              <tr>
                <td style={tdBold}>2. MIS (Management Information System)</td>
                <td style={tdStyle}>Level Manajerial<br /><i>(Pemilik Toko/Merchant)</i></td>
                <td style={tdStyle}>Mengubah data transaksi mentah TPS menjadi laporan analitik terstruktur dan grafik performa toko.</td>
                <td style={tdStyle}>• <b>Shopee Seller Centre Dashboard</b><br />• Grafik omzet & tren kata kunci</td>
                <td style={tdStyle}>Membantu merchant merencanakan persediaan stok barang secara tepat.</td>
              </tr>
              <tr>
                <td style={tdBold}>3. DSS (Decision Support System)</td>
                <td style={tdStyle}>Level Analitik Cerdas<br /><i>(Sistem AI & Analis)</i></td>
                <td style={tdStyle}>Menerapkan algoritma analitik prediktif dan Machine Learning untuk keputusan semi-terstruktur otomatis.</td>
                <td style={tdStyle}>• <b>AI Credit Scoring SPayLater</b><br />• Dynamic discount & rute kurir SPX</td>
                <td style={tdStyle}>Menekan rasio kredit macet (NPL) dan menghemat biaya rute kurir.</td>
              </tr>
              <tr>
                <td style={tdBold}>4. IOS (Inter-Organizational System)</td>
                <td style={tdStyle}>Lintas Organisasi<br /><i>(Shopee ↔ Bank ↔ Ekspedisi)</i></td>
                <td style={tdStyle}>Mengintegrasikan aliran data proses bisnis antar-perusahaan otomatis via B2B Open API.</td>
                <td style={tdStyle}>• Open API Virtual Account Bank<br />• Integrasi resi eksternal (J&T, SiCepat)</td>
                <td style={tdStyle}>Status pembayaran otomatis lunas seketika tanpa jeda manual.</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 9: TABEL 4 - ANALISIS EVALUASI PERANCANGAN SISTEM
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Tabel 4: Evaluasi SI"
        notes="Tabel keempat adalah Tabel Analisis Evaluasi Perancangan Sistem: Kelebihannya adalah skalabilitas microservices yang sangat tinggi saat 11.11 dan integrasi ekosistem yang rapat. Kelemahannya adalah terjadinya Application Bloatware yang membuat aplikasi berat dan nge-lag di HP spek rendah, serta latency saat flash sale. Celah keamanannya ada pada rekayasa sosial penipuan OTP. Saya merekomendasikan solusi Shopee Lite dan biometrik FIDO2 Passkeys."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Tabel Analisis 4 · Evaluasi Perancangan Sistem Informasi
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '10px',
            }}
          >
            Matriks Evaluasi: Kelebihan, Kelemahan, & Rekomendasi Solusi
          </h2>
        </Reveal>

        <div style={tableContainer}>
          <table style={tableStyle}>
            <thead>
              <tr>
                <th style={thStyle}>Dimensi Evaluasi</th>
                <th style={thStyle}>Temuan & Fakta Lapangan</th>
                <th style={thStyle}>Prinsip SI Terkait</th>
                <th style={thStyle}>Dampak / Risiko</th>
                <th style={thStyle}>Rekomendasi Solusi Saya</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style={tdBold}><span style={{ color: '#10b981' }}>1. Kelebihan (Strengths)</span></td>
                <td style={tdStyle}>• Skalabilitas microservices cloud tinggi.<br />• Integrasi ekosistem lock-in (belanja, paylater, kurir).<br />• Personalisasi rekomendasi belanja AI.</td>
                <td style={tdStyle}>• <i>Dapat Dikembangkan</i><br />• <i>Terintegrasi</i><br />• <i>User-Oriented</i></td>
                <td style={tdStyle}>Retensi pengguna sangat kuat & konversi penjualan tinggi.</td>
                <td style={tdStyle}>Pertahankan modularitas layanan mandiri dan perkuat ekosistem perbankan digital.</td>
              </tr>
              <tr>
                <td style={tdBold}><span style={{ color: '#ef4444' }}>2. Kelemahan (Weaknesses)</span></td>
                <td style={tdStyle}>• <b>Application Bloatware:</b> Kelebihan fitur non-core (games, video pendek, live stream).<br />• <b>Flash Sale Latency:</b> Antrean request timeout pada detik pertama promo 1 rupiah.</td>
                <td style={tdStyle}>• <i>Melanggar Prinsip Sederhana</i><br />• <i>Tantangan Prinsip Scalability</i></td>
                <td style={tdStyle}>Aplikasi boros memori RAM, lambat, dan baterai cepat panas di HP entry-level.</td>
                <td style={tdStyle}>Terapkan <b>Micro-Frontends</b> atau rilis resmi <b>Shopee Lite</b> (khusus core e-commerce).</td>
              </tr>
              <tr>
                <td style={tdBold}><span style={{ color: '#f59e0b' }}>3. Keamanan (Security)</span></td>
                <td style={tdStyle}>• <b>Social Engineering:</b> Pengguna awam rentan tertipu telepon/pesan oknum yang meminta kode SMS OTP.</td>
                <td style={tdStyle}>• <i>Celah Prinsip Aman (Human Factor)</i></td>
                <td style={tdStyle}>Pembobolan akun dan penyalahgunaan limit kredit SPayLater.</td>
                <td style={tdStyle}>Gantikan SMS OTP dengan otentikasi biometrik <b>FIDO2 Passkeys</b> (Sidik Jari / Face ID).</td>
              </tr>
            </tbody>
          </table>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 10: VALIDASI FAKTUAL
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Validasi Faktual"
        notes="Sebelum menutup, saya tegaskan bahwa seluruh data pada tabel analisis ini berlandaskan fakta resmi: Shopee Engineering Blog untuk arsitektur microservices Go/Java dan database Redis, Laporan Keterbukaan Sea Limited di bursa saham NYSE untuk data cloud Tencent dan AWS, Regulasi OJK untuk operasional SPayLater, serta ketentuan resmi Garansi Shopee."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Landasan Data & Validasi Akademik
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '14px',
            }}
          >
            Validasi Faktual: 4 Sumber Resmi Analisis Sistem Shopee
          </h2>
        </Reveal>

        <div
          style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))',
            gap: 16,
            alignItems: 'stretch',
          }}
        >
          <div style={card}>
            <div style={{ color: 'var(--primary)', fontWeight: 800, fontSize: 12, textTransform: 'uppercase', marginBottom: 6 }}>
              1. Shopee Engineering Blog
            </div>
            <p style={{ fontSize: 12.5, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Dokumentasi resmi arsitektur backend microservices Go/Java, caching in-memory Redis, dan distributed SQL TiDB.
            </p>
          </div>

          <div style={card}>
            <div style={{ color: '#0284c7', fontWeight: 800, fontSize: 12, textTransform: 'uppercase', marginBottom: 6 }}>
              2. Laporan Sea Limited (NYSE: SE)
            </div>
            <p style={{ fontSize: 12.5, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Laporan keterbukaan bursa saham yang memvalidasi infrastruktur cloud Tencent & AWS serta volume transaksi jutaan order per hari.
            </p>
          </div>

          <div style={card}>
            <div style={{ color: '#a855f7', fontWeight: 800, fontSize: 12, textTransform: 'uppercase', marginBottom: 6 }}>
              3. Regulasi OJK & Bank Indonesia
            </div>
            <p style={{ fontSize: 12.5, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Bukti legalitas SPayLater (PT Commerce Finance) dengan sistem scoring AI terhubung ke SLIK OJK dan Virtual Account bank.
            </p>
          </div>

          <div style={card}>
            <div style={{ color: '#059669', fontWeight: 800, fontSize: 12, textTransform: 'uppercase', marginBottom: 6 }}>
              4. Ketentuan Resmi Garansi Shopee
            </div>
            <p style={{ fontSize: 12.5, color: 'var(--fg-muted)', lineHeight: 1.5 }}>
              Mekanisme Rekening Penampung (Escrow Account) dan SLA kurir SPX Express yang membuktikan keandalan proses transaksi.
            </p>
          </div>
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 12: VIDEO
          ───────────────────────────────────────────────────────────── */}
      <Slide
        nav="Video"
        notes="Video pendukung presentasi."
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 6, textAlign: 'center' }}>
            Video Pendukung
          </div>
          <h2
            className="headline"
            style={{
              textAlign: 'center',
              marginInline: 'auto',
              fontSize: 'clamp(22px, 3vw, 36px)',
              marginBottom: '20px',
            }}
          >
            Video Presentasi
          </h2>
        </Reveal>

        <div
          style={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
          }}
        >
          <video
            src={`${BASE}video.mp4`}
            controls
            autoPlay
            style={{
              maxWidth: '100%',
              maxHeight: '60vh',
              borderRadius: 'var(--radius)',
              border: '1px solid var(--hair)',
              boxShadow: '0 4px 24px rgba(0,0,0,0.18)',
            }}
          />
        </div>
      </Slide>

      {/* ─────────────────────────────────────────────────────────────
          SLIDE 11: KESIMPULAN & Q&A
          ───────────────────────────────────────────────────────────── */}
      <Slide
        center
        nav="Penutup & Q&A"
        notes="Sebagai kesimpulan akhir: Penyajian dalam bentuk tabel analisis ini memperlihatkan bahwa arsitektur Sistem Informasi Shopee telah memenuhi prinsip integrasi, keamanan akses, dan skalabilitas tinggi. Namun penegakan prinsip kesederhanaan dan perlindungan dari rekayasa sosial tetap menjadi catatan kritis ke depan. Terima kasih banyak atas perhatian Bapak/Ibu dosen dan rekan-rekan, sesi tanya jawab saya buka!"
      >
        <Reveal>
          <div className="kicker" style={{ marginBottom: 12 }}>
            Sesi Diskusi Akademik
          </div>
          <h2
            className="headline"
            style={{ fontSize: 'clamp(28px, 4.2vw, 50px)', marginInline: 'auto', maxWidth: '26ch' }}
          >
            Terima Kasih atas <span className="accent-text">Perhatian Anda.</span>
          </h2>
          <p className="subhead" style={{ marginTop: 16, maxWidth: '36ch', marginInline: 'auto', fontSize: '1rem' }}>
            "Sistem Informasi yang unggul bukan sekadar yang paling canggih, melainkan yang paling sederhana, andal, dan menjawab kebutuhan nyata penggunanya."
          </p>
        </Reveal>
        <Build at={1}>
          <div style={{ marginTop: 28 }}>
            <span
              style={{
                display: 'inline-block',
                padding: '10px 24px',
                borderRadius: 'var(--radius-sm)',
                background: 'rgba(238, 77, 45, 0.15)',
                color: 'var(--primary)',
                fontWeight: 700,
                fontSize: 15,
                border: '1px solid rgba(238, 77, 45, 0.3)',
              }}
            >
              Silakan, Sesi Tanya Jawab (Q&A) Saya Buka 💬
            </span>
          </div>
        </Build>
      </Slide>
    </Deck>
  );
}
