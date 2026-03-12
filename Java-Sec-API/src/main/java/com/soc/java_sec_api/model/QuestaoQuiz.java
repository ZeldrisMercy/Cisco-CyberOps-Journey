package com.soc.java_sec_api.model;

import jakarta.persistence.*;

@Entity
@Table(name = "tb_questoes_quiz")
public class QuestaoQuiz {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "questao_id")
    private Integer questaoId;

    @Column(name = "modulo_id", nullable = false)
    private Integer moduloId;

    @Column(name = "pergunta", nullable = false)
    private String pergunta;

    @Column(name = "opcao_a", nullable = false)
    private String opcaoA;

    @Column(name = "opcao_b", nullable = false)
    private String opcaoB;

    @Column(name = "opcao_c", nullable = false)
    private String opcaoC;

    @Column(name = "opcao_d", nullable = false)
    private String opcaoD;

    @Column(name = "resposta_correta", nullable = false)
    private String respostaCorreta;

    @Column(name = "explicacao")
    private String explicacao;

    // Construtor vazio (obrigatório para o Spring/Hibernate)
    public QuestaoQuiz() {}

    // Getters
    public Integer getQuestaoId() { return questaoId; }
    public Integer getModuloId() { return moduloId; }
    public String getPergunta() { return pergunta; }
    public String getOpcaoA() { return opcaoA; }
    public String getOpcaoB() { return opcaoB; }
    public String getOpcaoC() { return opcaoC; }
    public String getOpcaoD() { return opcaoD; }
    public String getRespostaCorreta() { return respostaCorreta; }
    public String getExplicacao() { return explicacao; }
    
    // (Omiti os Setters aqui para o código ficar mais limpo, já que a API vai 
    // principalmente LER as questões, mas você pode gerar depois se for inserir via API)
}