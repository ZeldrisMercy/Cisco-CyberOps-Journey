package com.soc.java_sec_api.repository;

import com.soc.java_sec_api.model.ThreatLog;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ThreatLogRepository extends JpaRepository<ThreatLog, Integer> {
    
    // Olha a mágica: Só de escrever o nome do método seguindo o padrão do Spring,
    // ele automaticamente cria um "SELECT * FROM tb_threat_logs WHERE ip_origem = ?"
    List<ThreatLog> findByIpOrigem(String ipOrigem);
    
    // Outro exemplo automático: "SELECT * FROM tb_threat_logs WHERE status_resolucao = ?"
    List<ThreatLog> findByStatusResolucao(String statusResolucao);
}
