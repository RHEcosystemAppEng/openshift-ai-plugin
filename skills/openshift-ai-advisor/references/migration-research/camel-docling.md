# Camel Docling

Producer-only Red Hat build of Apache Camel for Spring Boot component (`camel-docling` / `camel-docling-starter`) that converts PDF/Office (and related) documents to Markdown/HTML/JSON/text via IBM Docling—CLI or `docling-serve` API—inside Camel routes (`to("docling:...")`). Detection category: **Camel document conversion for RAG**. Peers are DIY Camel PDF/Office extractors, standalone Docling without the Camel producer, and industry document parsers (Unstructured, LlamaParse, Marker, MinerU, managed OCR APIs) that teams use instead of (or before) adopting **Camel Docling**.

## Peers

- DIY PDFBox / Tika / POI in Camel — Apache PDFBox, Apache Tika, or `poi-ooxml` (plus hand-rolled text extract) in Camel routes before `camel-openai` / vector components; classic “should use camel-docling” pattern
- Docling standalone (no Camel) — Python `DocumentConverter` / `pip install docling`, notebooks, LangChain `DoclingLoader` / `langchain-docling`, or direct `docling-serve` HTTP without `camel-docling`
- Java ProcessBuilder / HTTP to Docling outside the component — shell-out to `docling` CLI or RestTemplate/WebClient/`docling-java` calls to `:5001` from Spring Boot/Quarkus **without** URI `docling:`
- Unstructured — `unstructured` / Unstructured.io (`partition_pdf`, `UnstructuredFileLoader`, hi-res layout) as the org RAG ingest parser
- LlamaParse — LlamaCloud / LlamaIndex hosted PDF→Markdown API (`LlamaParse`, `llama_parse`, `llama-cloud-services`)
- Marker — Datalab Marker PDF→Markdown/JSON (`marker-pdf`, `datalab-to/marker`) for speed-first academic/text-heavy corpora
- MinerU — OpenDataLab MinerU / MinerU2.x VLM document parsers (`opendatalab/MinerU`) competing on table/layout quality
- Firecrawl / crawl-to-markdown ETL — Firecrawl (and similar web/doc→Markdown services) used as the ingest converter instead of layout-aware Docling
- Naive PDF loaders — PyPDF / `pypdf` / pdfplumber / PyMuPDF4LLM / LangChain `PyPDFLoader` alone for born-digital prose (weak structure; same need class when teams are about to upgrade)
- Managed document intelligence APIs — Azure Document Intelligence / Form Recognizer, AWS Textract, Google Document AI, Mistral OCR, Reducto as SaaS stand-ins for layout-aware conversion

**Not peers (adjacent catalog jobs):** **RAG Stack** / **Llama Stack** (full managed chunk→embed→retrieve unit, not a Camel conversion producer); **camel-openai** / Camel vector components alone (embeddings/stores without a document-conversion step); treating a bare **docling-serve** Deployment as the catalog product (serve is runtime; catalog item is the Camel producer).

## Detection aliases

- DIY PDFBox / Tika / POI in Camel: `org.apache.pdfbox`, `PDFTextStripper`, `org.apache.tika`, `Tika()`, `poi-ooxml`, `XWPFDocument`, `XMLSlideShow`; Camel `file:`/`aws2-s3:`/`kafka:` ingest → hand extract → embed/vector without `camel-docling`
- Docling standalone: `pip install docling`, `from docling.document_converter import DocumentConverter`, `export_to_markdown()`, `langchain-docling`, `DoclingLoader`, `HybridChunker`; `docling-serve` / `ghcr.io/docling-project/docling-serve` / `:5001` **without** `useDoclingServe` + `docling:` URIs
- Java outside component: `ProcessBuilder` + `docling`, RestTemplate/WebClient/`docling-java` to `/v1/convert/file` or `/v1/convert/source` without Maven `camel-docling`
- Unstructured: `unstructured`, `unstructured-ingest`, `partition_pdf`, `partition_auto`, `UnstructuredFileLoader`, `hi_res`, Unstructured-IO
- LlamaParse: `LlamaParse`, `llama_parse`, `LLAMA_CLOUD_API_KEY`, `llama-parse`, `llama-cloud-services`, `LlamaCloud`
- Marker: `marker-pdf`, `marker_single`, `from marker`, `datalab-to/marker`, Marker convert PDF to markdown
- MinerU: `mineru`, `MinerU`, `opendatalab/MinerU`, `magic-pdf`
- Firecrawl / crawl ETL: `firecrawl`, `FIRECRAWL_API_KEY`, crawl-to-markdown ingest jobs
- Naive PDF loaders: `pypdf`, `PyPDFLoader`, `pdfplumber`, `pymupdf`, `PyMuPDF4LLM`, `fitz.open`
- Managed OCR/DI APIs: Azure `DocumentIntelligenceClient` / Form Recognizer; `textract`; Google Document AI; `mistral-ocr` / Mistral OCR; Reducto parse API
- Need-for-component language: “convert PDF to Markdown in Camel”, “Docling for RAG ingestion”, “IBM Docling in integration route”; RH Camel 4.18 AI features listing document conversion without `camel-docling` yet

## Row for `Camel Docling`

| DIY PDFBox/Tika/POI in Camel; Docling standalone (no Camel); Java ProcessBuilder/HTTP to Docling outside camel-docling; Unstructured; LlamaParse; Marker; MinerU; Firecrawl/crawl-to-markdown ETL; naive PyPDF/pdfplumber/PyMuPDF loaders; Azure Document Intelligence / AWS Textract / Google Document AI / Mistral OCR / Reducto | Camel Docling | DIY PDFBox/Tika/POI in Camel: org.apache.pdfbox / PDFTextStripper / org.apache.tika / Tika() / poi-ooxml / XWPFDocument; Docling standalone: DocumentConverter / export_to_markdown / langchain-docling / DoclingLoader / docling-serve :5001 without docling: URIs; Java outside component: ProcessBuilder docling / RestTemplate docling-java /v1/convert; Unstructured: unstructured / partition_pdf / UnstructuredFileLoader / hi_res; LlamaParse: LlamaParse / llama_parse / LLAMA_CLOUD_API_KEY; Marker: marker-pdf / datalab-to/marker; MinerU: mineru / opendatalab/MinerU; Firecrawl: firecrawl / FIRECRAWL_API_KEY; Naive loaders: pypdf / PyPDFLoader / pdfplumber / PyMuPDF4LLM; Managed DI: DocumentIntelligenceClient / textract / Document AI / Mistral OCR / Reducto |
