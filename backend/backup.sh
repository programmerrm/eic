#!/bin/bash

DATE=$(date +%F)
BACKUP_ROOT="/opt/backups"
BACKUP_DIR="$BACKUP_ROOT/$DATE"

POSTGRES_DB="pngdb"
POSTGRES_USER="pnguser"
POSTGRES_HOST="localhost"

MEDIA_DIR="/app/media"

REDIS_DUMP="/var/lib/redis/dump.rdb"

echo "🚀 Backup started: $DATE"
mkdir -p "$BACKUP_DIR"

# ===== PostgreSQL Backup =====
pg_dump -h "$POSTGRES_HOST" -U "$POSTGRES_USER" "$POSTGRES_DB" | gzip > "$BACKUP_DIR/db.sql.gz"

# ===== Media Backup =====
tar -czf "$BACKUP_DIR/media.tar.gz" "$MEDIA_DIR"

# ===== Redis Backup (optional) =====
redis-cli save
cp "$REDIS_DUMP" "$BACKUP_DIR/redis.rdb"

# ===== Keep only last 3 days =====
find "$BACKUP_ROOT" -mindepth 1 -maxdepth 1 -type d -mtime +2 -exec rm -rf {} \;

echo "✅ Backup completed & old backups removed"
