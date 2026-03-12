package com.soc.java_sec_api.model;

import jakarta.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "tb_threat_logs")
public class ThreatLog {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY) 
    @Column(name = "log_id")
    private Integer logId;

    @Column(name = "ip_origem", nullable = false)
    private String ipOrigem;

    @Column(name = "tentativas_falhas", nullable = false)
    private Integer tentativasFalhas;

    @Column(name = "status_resolucao", nullable = false)
    private String statusResolucao;

    @Column(name = "data_incidente", insertable = false, updatable = false)
    private LocalDateTime dataIncidente; 

    @Column(name = "ferramenta_origem")
    private String ferramentaOrigem;

    // =========================================================
    // Construtor Vazio (Exigência do Hibernate)
    // =========================================================
    public ThreatLog() {
    }

    // =========================================================
    // Getters e Setters (Para o Java poder ler e gravar os dados)
    // =========================================================
    public Integer getLogId() { return logId; }
    public void setLogId(Integer logId) { this.logId = logId; }

    public String getIpOrigem() { return ipOrigem; }
    public void setIpOrigem(String ipOrigem) { this.ipOrigem = ipOrigem; }

    public Integer getTentativasFalhas() { return tentativasFalhas; }
    public void setTentativasFalhas(Integer tentativasFalhas) { this.tentativasFalhas = tentativasFalhas; }

    public String getStatusResolucao() { return statusResolucao; }
    public void setStatusResolucao(String statusResolucao) { this.statusResolucao = statusResolucao; }

    public LocalDateTime getDataIncidente() { return dataIncidente; }
    public void setDataIncidente(LocalDateTime dataIncidente) { this.dataIncidente = dataIncidente; }

    public String getFerramentaOrigem() { return ferramentaOrigem; }
    public void setFerramentaOrigem(String ferramentaOrigem) { this.ferramentaOrigem = ferramentaOrigem; }
}