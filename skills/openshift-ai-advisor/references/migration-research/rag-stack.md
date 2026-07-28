# RAG Stack Deployment

Catalog: administrator-driven unit that provisions a full RAG pipeline — LLM inference (vLLM), PostgreSQL+pgvector, embedding service, and retrieval endpoints — so project teams avoid assembling the stack themselves (OGX / Llama Stack RAG). Detection category: **RAG application patterns**. Peers are DIY framework RAG apps, self-hosted vector+embed+LLM Compose/Helm stacks, managed knowledge-base products, and hand-rolled `/ask`|`/retrieve`|`/ingest` APIs that teams run instead of (or before) adopting RHOAI RAG Stack Deployment.

## Peers

- LangChain DIY RAG — loaders + `RecursiveCharacterTextSplitter` + Chroma/FAISS/pgvector/Pinecone + `as_retriever` / `create_retrieval_chain` / legacy `RetrievalQA`
- LlamaIndex DIY RAG — `VectorStoreIndex`, `IngestionPipeline`, `as_query_engine` / `as_retriever` with Qdrant/Milvus/Pinecone/Weaviate/Chroma/PGVector stores
- Haystack — deepset pipelines (`DocumentStore`, `EmbeddingRetriever` / `InMemoryEmbeddingRetriever`, `Pipeline` RAG nodes) + Elasticsearch/OpenSearch/Qdrant/Weaviate backends
- Custom Chroma stack — `chromadb` PersistentClient/HttpClient or `chromadb/chroma` Compose next to embed + LLM + retrieval API
- Custom FAISS stack — `faiss-cpu`/`faiss-gpu`, on-disk `.faiss`/`index.pkl`, notebook or service-side similarity search without a managed vector DB
- Custom pgvector / PostgreSQL stack — `pgvector/pgvector`, `CREATE EXTENSION vector`, LangChain `PGVector` / DIY SQL `<=>`/`<->` retrieval
- Milvus / Qdrant / Weaviate DIY stacks — Compose/Helm `milvusdb/milvus`, `qdrant/qdrant`, `semitechnologies/weaviate` + app-side embed/retrieve
- Pinecone (managed vector) DIY apps — app-owned ingest/chunk/embed/retrieve against `PINECONE_API_KEY` indexes (no RHOAI RAG unit)
- Compose / Helm multi-service RAG — vector DB + embedding container + LLM (vLLM/TGI/Ollama) + FastAPI `/ask`|`/retrieve`|`/ingest` in one chart
- Custom FastAPI/Flask retrieval APIs — hand-rolled embed → search → prompt-LLM services (`SentenceTransformer`, `/v1/embeddings`, `ingest.py`)
- Verba / PrivateGPT / AnythingLLM — self-hosted “chat with docs” apps bundling ingest + vector + LLM outside RHOAI
- Dify / Flowise / Langflow — low-code RAG builders with their own vector/LLM connectors
- Amazon Bedrock Knowledge Bases / Azure AI Search RAG / Vertex AI RAG Engine — managed cloud RAG/knowledge-base products
- Elasticsearch / OpenSearch kNN + BM25 hybrid DIY — ELSER/dense vector indexes feeding custom RAG apps

## Detection aliases

- LangChain RAG: `langchain`, `langchain-community`, `langchain-chroma`, `RecursiveCharacterTextSplitter`, `RetrievalQA`, `create_retrieval_chain`, `create_stuff_documents_chain`, `vectorstore.as_retriever`, `FAISS.from_documents`, `PGVector` / `Chroma` / `PineconeVectorStore` from `langchain*`
- LlamaIndex RAG: `llama-index`, `llama-index-core`, `VectorStoreIndex`, `SimpleDirectoryReader`, `IngestionPipeline`, `as_query_engine(`, `QdrantVectorStore` / `MilvusVectorStore` / `ChromaVectorStore` / `PGVectorStore`
- Haystack: `haystack-ai`, `haystack`, `from haystack`, `DocumentStore`, `EmbeddingRetriever`, `Pipeline().add_component`, `InMemoryDocumentStore`
- Chroma: `chromadb`, `PersistentClient`, `HttpClient`, `chromadb/chroma`, `ghcr.io/chroma-core/chroma`, `chroma.sqlite3`, port `:8000`
- FAISS: `faiss-cpu`, `faiss-gpu`, `import faiss`, `.faiss`, `index.faiss`, `index.pkl`, `allow_dangerous_deserialization`
- pgvector: `pgvector/pgvector`, `CREATE EXTENSION vector`, SQL `vector(`, `<=>` / `<->` / `<#>`, `USING hnsw` / `ivfflat`, package `pgvector`
- Milvus / Qdrant / Weaviate: `pymilvus`, port `19530`, `milvusdb/milvus`; `qdrant-client`, `qdrant/qdrant`, `:6333`; `weaviate-client`, `semitechnologies/weaviate`
- Pinecone: `pinecone`, `Pinecone(`, `PINECONE_API_KEY`, `PINECONE_INDEX_NAME`, `ServerlessSpec`
- DIY infra / APIs: `docker-compose`/`compose.yaml` with vector+embed+LLM; FastAPI routes `/ask`, `/query`, `/retrieve`, `/ingest`; `SentenceTransformer(`, `all-MiniLM-L6-v2`, `ingest.py`; MinIO/S3 corpus staging
- Packaged RAG apps / builders: `verba`, `private-gpt`/`privategpt`, `anythingllm`, `dify`, `flowise`, `langflow`
- Cloud managed RAG: `bedrock` Knowledge Base / `RetrieveAndGenerate`; Azure AI Search `SearchClient` + RAG; Vertex `RagManagedDb` / Vertex AI Search grounding
- Hybrid search DIY: `rank_bm25`, Elasticsearch/OpenSearch kNN + keyword, `CrossEncoder` / Cohere Rerank

## Row for `RAG Stack Deployment`

| LangChain DIY RAG; LlamaIndex DIY RAG; Haystack; custom Chroma/FAISS/pgvector stacks; Milvus/Qdrant/Weaviate DIY; Pinecone-backed DIY apps; Compose/Helm vector+embed+LLM RAG; custom FastAPI /ask|/retrieve|/ingest; Verba/PrivateGPT/AnythingLLM; Dify/Flowise/Langflow; Bedrock Knowledge Bases / Azure AI Search RAG / Vertex AI RAG Engine; Elasticsearch/OpenSearch hybrid DIY | RAG Stack Deployment | langchain / RecursiveCharacterTextSplitter / RetrievalQA / create_retrieval_chain / as_retriever; llama-index / VectorStoreIndex / as_query_engine / IngestionPipeline; haystack-ai / DocumentStore / EmbeddingRetriever; chromadb / chromadb/chroma; faiss-cpu / index.faiss; pgvector/pgvector / CREATE EXTENSION vector; pymilvus / qdrant-client / weaviate-client; PINECONE_API_KEY; compose vector+embed+LLM; FastAPI /ask|/retrieve|/ingest; SentenceTransformer / ingest.py; verba / privategpt / dify / flowise / langflow; bedrock Knowledge Bases / Azure AI Search / Vertex RAG; rank_bm25 / CrossEncoder |
